from loguru import logger
from webdriver_manager.chrome import ChromeDriverManager

from helper.timer import timer 
from scripts.selenium import SeleniumScraper
from scripts.playwright import PlaywrightScraper



def main() -> None:
    # Download latest chromedriver and get it's path
    logger.info("Fetch chromedriver...")
    chromedriver_path = ChromeDriverManager().install()
    
    # Run Selenium
    selenium_scraper = SeleniumScraper(chromedriver_path)
    selenium_time = timer(selenium_scraper)
    
    # Run Playwright
    playwright_scraper = PlaywrightScraper()
    playwright_time = timer(playwright_scraper)
    
    # Compare each other runtimes
    logger.info(f"Selenium scraping time : {selenium_time} ns")
    logger.info(f"Playwright scraping time : {playwright_time} ns")
    
    if playwright_time < selenium_time:
        logger.info(f"Playwright {selenium_time/playwright_time:.2%} faster than Selenium.")
    else:
        logger.info(f"Selenium {playwright_time/selenium_time:.2%}% faster than Playwright.")
    
if __name__ == "__main__":
    main()