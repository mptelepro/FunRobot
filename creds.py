import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Credentials:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # Take it from @botfather
    API_ID = int(os.getenv("API_ID"))  # take it from https://my.telegram.org/apps
    API_HASH = os.getenv("API_HASH")  # take it from  https://my.telegram.org/apps
    CHAT_GROUPS = os.getenv("CHAT_GROUPS") # enter the Username or Id of Groups where you want the bot to work !!
