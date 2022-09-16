from dataclasses import dataclass
from typing import List

from loguru import logger
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from env import TARGET_URL
from scripts.scraper import Scraper 


@dataclass
class SeleniumScraper(Scraper):
    driver_path: str    # Chromedriver path

    def __post_init__(self):
        logger.info("Initiate Selenium Scraper.")
        
        # Set driver options
        chrome_options = webdriver.ChromeOptions()

        # Add arguments
        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.default_content_setting_values.notifications": 2
            }
        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--incognito")
        
        # Create web driver object
        service = Service(self.driver_path)
        self.driver = webdriver.Chrome(
            service=service,
            options=chrome_options
        )
        
    def wait_until_element_visible(
            self,
            locator: str,
            locator_value: str,
            timeout: int = 15
        ) -> None:
        """
        Wait until specified element is located or timeout is exceeded.

        Args:
            locator (str):  Locator string, or use Selenium `By` attributes. 
                            These are the attributes available for By class:
                                            
                            ID = "id"
                            XPATH = "xpath"
                            LINK_TEXT = "link text"
                            PARTIAL_LINK_TEXT = "partial link text"
                            NAME = "name"
                            TAG_NAME = "tag name"
                            CLASS_NAME = "class name"
                            CSS_SELECTOR = "css selector"
            
            locator_value (str): Specific element value based on locator type.
            timeout (int, optional): Timeout in seconds. Defaults to 15.
        """
        
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located((locator, locator_value)))
        
    def find_elements(
            self,
            locator: str,
            locator_value: str,
            timeout: int = 15
        ) -> List[WebElement]:
        """
        Find multiple web elements by specific locator and value.

        Args:
            locator (str):  Locator string, or use Selenium `By` attributes. 
                            These are the attributes available for By class:
                                            
                            ID = "id"
                            XPATH = "xpath"
                            LINK_TEXT = "link text"
                            PARTIAL_LINK_TEXT = "partial link text"
                            NAME = "name"
                            TAG_NAME = "tag name"
                            CLASS_NAME = "class name"
                            CSS_SELECTOR = "css selector"
            
            locator_value (str): Specific element value based on locator type.
            timeout (int, optional): Timeout in seconds. Defaults to 15.

        Returns:
            WebElement: Selenium web element.
        """  
        self.wait_until_element_visible(locator, locator_value, timeout)
        elements = self.driver.find_elements(locator, locator_value)
        
        return elements
        
    def scrape(self) -> List[str]:
        """Extract latest trends from Google Trends ID.

        Returns:
            List[str]: List of Google Trends topics string.
        """
        self.driver.get(TARGET_URL)
        trend_elements = self.find_elements(By.CSS_SELECTOR, 'div.details-top')
        trends = [t.text for t in trend_elements]
        self.driver.quit()
        logger.info("Selenium done scraping.")
        
        return trends
        