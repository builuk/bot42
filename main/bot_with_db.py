from datetime import datetime, timedelta
from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.user_service import check_user_role
from services.database_service import Database
from config.env_config import *
from helper.handler_helper import CommandHandlerFactory
import requests
import json
from datetime import datetime, timedelta



# Оновлення check_user_role для використання бази даних
def check_user_db_role(user_id):
    if user_id == ADMIN_ID:
        return 'admin'
    db = Database()
    role_data = db.get_user_roles(user_id)
    role = extract_unique_word(role_data)

    if role:
        print(role)
        return role
    else:
        print(role)
        # За замовчуванням додаємо роль "guest"
        db.add_user_role(user_id, "guest")
        return "guest"


def extract_unique_word(role_data):
    if isinstance(role_data, list) and len(role_data) == 1:
        return role_data[0]
    return None


def main_loop(duration_minutes=1):
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    offset = 0
    last_reported_minute = None
    print(f"Bot started. Running for {duration_minutes} minutes...")

    while datetime.now() < end_time:
        response = requests.get(API_URL + f"getUpdates?offset={offset}")
        updates = response.json().get('result', [])
        for update in updates:
            offset = update['update_id'] + 1
            message = update.get('message')
            if message and 'text' in message:
                user_id = str(message['from']['id'])
                role = check_user_db_role(user_id)
                handler = CommandHandlerFactory().get_handler(role)
                handler.handle(message)

    print("Bot finished running.")


if __name__ == "__main__":
    main_loop()