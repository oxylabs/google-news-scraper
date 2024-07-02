"""
    Module for parsing Google News HTML content.
"""

from typing import List
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from google_news_scraper.conf import google_news_scraper_settings
from google_news_scraper.models import Article


class GoogleNewsHTMLParser:
    """Class for parsing Google News HTML content."""

    def _parse_article(self, article: BeautifulSoup) -> Article | None:
        """Parses single Google News article from extracted HTML"""
        title = article.find("a", {"class": "gPFEn"})
        title_text = title.get_text(strip=True) if title else None
        url = (
            urljoin(google_news_scraper_settings.url, title.get("href"))
            if title
            else None
        )
        if not any((title_text, url)):
            return None

        return Article(title=title_text, url=url)

    def parse(self, html: str) -> List[Article]:
        """
        Parses HTML content from Google News into a list of Article objects.

        Args:
            html (str): HTML content from a Google News page.

        Returns:
            List[Article]: A list of Article objects.
        """
        soup = BeautifulSoup(html, "html.parser")
        articles: List[BeautifulSoup] = soup.find_all(
            "c-wiz", {"class": "PO9Zff Ccj79 kUVvS"}
        )
        return [
            parsed_article
            for article in articles
            if (parsed_article := self._parse_article(article))
        ]
