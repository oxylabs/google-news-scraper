"""
    Config module for google_news_scraper.
"""

from urllib.parse import urljoin

from pydantic_settings import BaseSettings


class GoogleNewsScraperSettings(BaseSettings):
    """Settings class for Google News Scraper"""

    url: str = "https://news.google.com/"

    def get_url_for_topic(self, topic_id: str) -> str:
        return urljoin(self.url, f"topics/{topic_id}?hl=en-US&gl=US&ceid=US%3Aen")


google_news_scraper_settings = GoogleNewsScraperSettings()
