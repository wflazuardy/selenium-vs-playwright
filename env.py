from os import getenv
from dotenv import load_dotenv


# Set values from .env to environment variables 
load_dotenv()

# Load encironment variables
TARGET_URL = getenv("TARGET_URL", "https://trends.google.com/trends/trendingsearches/daily?geo=ID")
