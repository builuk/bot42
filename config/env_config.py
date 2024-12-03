from dotenv import dotenv_values
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

API_URL = f"https://api.telegram.org/bot{TOKEN}/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))