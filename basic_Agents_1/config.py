# Load OpenAI API key from .env file
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
