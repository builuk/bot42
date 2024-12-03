from handlers.base_handler import CommandHandler
from services.message_service import send_message
from services.user_service import check_user_role
from config.env_config import *
from helper.handler_helper import CommandHandlerFactory
import requests


def main_loop():
    offset = 0
    while True:
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


if __name__ == "__main__":
    main_loop()
