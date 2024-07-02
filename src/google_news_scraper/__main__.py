"""
    Main module for google_news_scraper.
"""

import logging

import click

from google_news_scraper.scraper import GoogleNewsScraper


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--topic", help="The ID of the Google News topic to scrape.", required=True
)
def scrape_google_news(topic: str) -> None:
    scraper = GoogleNewsScraper()
    scraper.scrape(topic)


if __name__ == "__main__":
    scrape_google_news()
