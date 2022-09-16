from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class Scraper(ABC):
    """
    Base abstract class for all scraper objects.
    """
    
    @abstractmethod
    def scrape(self) -> List[str]:
        ...