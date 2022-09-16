from time import time_ns
from typing import Type

from scripts.scraper import Scraper

def timer(scraper: Scraper) -> int:
    """Get excecution time of Scraper object's
    scraping runtime.

    Args:
        scraper (Scraper): Scraper object.

    Returns:
        int: Execution time in nanoseconds
    """
    start = time_ns()
    scraper.scrape()
    end = time_ns()
    
    return end - start