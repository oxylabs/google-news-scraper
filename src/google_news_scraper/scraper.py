"""
    Main module for scraping and storing Google News data.
"""

import logging

from typing import List

import httpx
import pandas as pd

from google_news_scraper.conf import google_news_scraper_settings
from google_news_scraper.cookies import GoogleNewsCookieRetriever
from google_news_scraper.models import Article
from google_news_scraper.parser import GoogleNewsHTMLParser


DEFAULT_OUTPUT_FILE = "articles.csv"


class GoogleNewsConnectionError(BaseException):
    message = "Unable to access Google News for getting HTML content."


class GoogleNewsGetHTMLError(BaseException):
    message = "Unable to get HTML content from Google News."


class GoogleNewsScraper:
    """Class for scraping Google News data"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._cookie_retriever = GoogleNewsCookieRetriever()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive",
        }
        self._logger = logger if logger else logging.getLogger(__name__)
        self._parser = GoogleNewsHTMLParser()

    def _save_to_csv(self, articles: List[Article]) -> None:
        """Saves given list of articles to a CSV file."""
        self._logger.info(f"Writing {len(articles)} articles to {self._output_file}..")
        article_objects = [article.model_dump() for article in articles]
        df = pd.DataFrame(article_objects)
        df.to_csv(self._output_file)

    def scrape(self, topic_id: str) -> None:
        """
        Scrapes data from a Google News topic and stores it to a CSV file.

        Args:
            topic_id (str): The ID of a Google News topic to scrape.
        Raises:
            GoogleNewsConnectionError: Unable to establish connection with Google News.
            GoogleNewsGetHTMLError: Unable to retrieve HTML content due to bad status code.
        """
        self._logger.info(f"Scraping topic {topic_id}..")
        cookies = self._cookie_retriever.get_consent_cookies()
        if not cookies:
            self._logger.warning("Got empty consent cookies. Scraping might fail.")

        try:
            response = httpx.get(
                google_news_scraper_settings.get_url_for_topic(topic_id),
                headers=self._headers,
                cookies=cookies,
            )
            response.raise_for_status()
        except httpx.RequestError as e:
            raise GoogleNewsConnectionError from e
        except httpx.HTTPStatusError as e:
            raise GoogleNewsGetHTMLError from e

        html_content = response.text
        articles = self._parser.parse(html_content)
        self._save_to_csv(articles)
