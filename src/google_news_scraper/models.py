"""
    Pydantic models for Google News scraper.
"""

from pydantic import BaseModel


class Article(BaseModel):
    title: str | None
    url: str | None
