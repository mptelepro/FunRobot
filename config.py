import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("1696386360:AAFMPYEKS5tdF7vY9UUrbyaPcsKEJq5-TNY", "")

    APP_ID = int(os.environ.get("3454845", 12345))

    API_HASH = os.environ.get("a205de875f47541dfa6b213bdfe56d36", "")

    CHAT_GROUPS = os.environ.get("1001239208195", "")

    OWNER_ID = os.environ.get("1650092910", "")
