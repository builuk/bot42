from dotenv import dotenv_values
from dotenv import load_dotenv
import os

# config = dotenv_values("../.env")
# TOKEN = config.get('TOKEN')
# ADMIN_ID = config.get('ADMIN_ID')
load_dotenv()
TOKEN = os.getenv("TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")
# TOKEN = '7800222511:AAHsM7pQUjnKr655TD9TuZI1kgZGQEgP4Do'
# ADMIN_ID = "259158244"
API_URL = f"https://api.telegram.org/bot{TOKEN}/"
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config'))