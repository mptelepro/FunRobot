import logging
from pyrogram import Client
from Config import Config

logging.basicConfig(level=logging.INFO)

plugins = dict(
    root="main",
    include=[
        "main",
        "main"
    ]
)

app = Client(
     'FunRobot',
      bot_token = Config.BOT_TOKEN,
      api_id = Config.API_ID,
      api_hash = Config.API_HASH,
      main = main
)

app.run()
