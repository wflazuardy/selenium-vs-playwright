from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager

from helper.timer import timer 
from scripts.selenium import SeleniumScraper


def main() -> None:
    # Download latest chromedriver and get it's path
    logger.info("Fetch chromedriver...")
    chromedriver_path = ChromeDriverManager().install()
    
    # Run Selenium
    selenium_scraper = SeleniumScraper(chromedriver_path)
    selenium_time = timer(selenium_scraper)
    
    logger.info(f"Selenium scraping time : {selenium_time} ns")
    
if __name__ == "__main__":
    main()