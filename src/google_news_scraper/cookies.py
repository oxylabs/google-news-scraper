"""
    Module for retrieving necessary cookies for scraping Google News.
"""

import logging
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from google_news_scraper.conf import google_news_scraper_settings
from google_news_scraper.exception import BaseException


logging.getLogger("WDM").setLevel(logging.ERROR)


class UnableToRetrieveConsentCookieError(BaseException):
    message = "Error when retrieving consent cookie for Google News"


class GoogleNewsCookieRetriever:
    """Class for retrieving cookies for Google News"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _retrieve_consent_cookie_with_driver(
        self, driver: webdriver.Chrome
    ) -> dict | None:
        """Retrieves consent cookie from Google with selenium Chrome webdriver"""
        driver.get(google_news_scraper_settings.url)
        try:
            consent_button = driver.find_element(
                By.XPATH,
                self._consent_button_xpath,
            )
            consent_button.click()
        except Exception:
            self._logger.error(
                "Unable to click Google consent button with selenium. Can't retrieve cookies."
            )
            return None

        time.sleep(7)

        cookies = driver.get_cookies()
        socs_cookie = next(
            (cookie for cookie in cookies if cookie["name"] == "SOCS"), None
        )
        if not socs_cookie:
            self._logger.error("Unable to find consent cookie from retrieved cookies.")
            return None

        try:
            cookie_value = socs_cookie["value"]
        except KeyError:
            self._logger.error("Received cookie with no value.")
            return None

        return {"SOCS": cookie_value}

    def get_consent_cookies(self) -> dict | None:
        """
        Retrieves cookies that indicate a completed Google consent form.

        Returns:
            dict | None: The retrieved consent cookies. Empty if cookie retrieval failed.
        """
        self._logger.info("Retrieving consent cookies..")

        try:
            driver = self._init_chrome_driver()
        except Exception:
            self._logger.exception(
                "Unable to initialize selenium webdriver for cookie retrieval. Returning None.."
            )
            return None

        try:
            return self._retrieve_consent_cookie_with_driver(driver)
        finally:
            driver.close()
