from dataclasses import dataclass
from typing import List

from loguru import logger
from playwright.sync_api import sync_playwright

from env import TARGET_URL
from scripts.scraper import Scraper


@dataclass
class PlaywrightScraper(Scraper):
    def scrape(self) -> List[str]:
        """Extract latest trends from Google Trends ID.

        Returns:
            List[str]: List of Google Trends topics string.
        """
        logger.info("Initiate Playwright Scraper.")
        with sync_playwright() as p:
            # Launch chromium driver
            driver = p.chromium.launch()
            
            # Open a webpage & instantiate page object
            page = driver.new_page()
            page.goto(TARGET_URL)
            
            # Get all trends
            trend_elements = page.query_selector_all("div.details-top")
            trends = [t.inner_text() for t in trend_elements]
            driver.close()
            
            return trends