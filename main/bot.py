from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.user_service import check_user_role
from config.env_config import *
from helper.handler_helper import CommandHandlerFactory
import requests
from datetime import datetime, timedelta


def main_loop(duration_minutes=6):
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    offset = 0
    last_reported_minute = None
    print(f"Bot started. Running for {duration_minutes} minutes...")

    while datetime.now() < end_time:
        remaining_minutes = (end_time - datetime.now()).seconds // 60
        if last_reported_minute != remaining_minutes:
            print(f"Time remaining: {remaining_minutes} minutes")
            last_reported_minute = remaining_minutes
        response = requests.get(API_URL + f"getUpdates?offset={offset}")
        updates = response.json().get('result', [])
        for update in updates:
            offset = update['update_id'] + 1
            message = update.get('message')
            if message and 'text' in message:
                user_id = str(message['from']['id'])
                role = check_user_role(user_id)
                handler = CommandHandlerFactory().get_handler(role)
                handler.handle(message)

    print("Bot finished running.")


if __name__ == "__main__":
    main_loop()
    print("Bot finished running.")
    print()
