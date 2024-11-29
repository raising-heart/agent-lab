# config.py - Handles environment configuration

import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()  # Load environment variables from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
