from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager

from scripts.selenium import SeleniumScraper


def main() -> None:
    # Download latest chromedriver and get it's path
    logger.info("Fetch chromedriver...")
    chromedriver_path = ChromeDriverManager().install()
    
    # Run Selenium
    SeleniumScraper(chromedriver_path).scrape()
    
if __name__ == "__main__":
    main()