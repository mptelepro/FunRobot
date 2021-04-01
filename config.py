import os


class Config(object):
    BOT_TOKEN = os.environ.get("bot_token:", "")

    APP_ID = int(os.environ.get("api_id", 12345))

    API_HASH = os.environ.get("api_hash", "")

    CHAT_GROUPS = os.environ.get("CHATSTOWORK", "")

    OWNER_ID = os.environ.get("OWNERID", "")
