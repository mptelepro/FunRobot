import os
import uuid
import shutil
import logging
import random
import pyjokes
from pyrogram import Client, filters
from creds import Credentials
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
logging.basicConfig(level=logging.INFO)


FunBot = Client(
    "Fun Robot",
    bot_token=Credentials.BOT_TOKEN,
    api_id=Credentials.API_ID,
    api_hash=Credentials.API_HASH,
)

CHATSTOWORK = Credentials.CHAT_GROUPS
SARCASM = pyjokes.get_joke()

@FunBot.on_message(filters.command("start") & filters.group)
async def start(client, message):
    await message.reply_text(
        f"**Hi, I am FunBot. I can Perform Many Task For You. To know then send `/help`**",
        True,
        reply_markup=InlineKeyboardMarkup[[InlineKeyboardButton(text="Updates Channel", url="t.me/prothinkergang")],
                                          [InlineKeyboardButton(text="Deploy Your Own Bot",url="#ToDo")]
                                          ]
    )

diceoutput = random.randrange(1,6)

@FunBot.on_message(filters.command("dice") & filters.chat(f'{CHATSTOWORK}'))
async def throwdice(client, message):
    await message.reply_text(f"**Dice Thrown !\n\nOuput\n==>>'{diceoutput}'**",True)
    
@FunBot.on_message(filters.command("vdice") & filters.chat(f'{CHATSTOWORK}'))
async def throwdice(client, message):
    await message.reply_text("🎲",True)

@FunBot.on_message(filters.command("vjackpot") & filters.chat(f'{CHATSTOWORK}'))
async def throwdice(client, message):
    await message.reply_text("🎰",True)
    
@FunBot.on_message(filters.command("jokes") & filters.chat(f'{CHATSTOWORK}'))
async def throwdice(client, message):
    await message.reply_text(f"`{SARCASM}`",True)
    
Dechoices = ("Yes","No","Surely Yes","Maybe","Nooo.","God Knows","Cant decide")
oploa = random.randrange(0,len(Dechoices)-1)
Secom = Dechoices[oploa]
    
@FunBot.on_message(filters.command("decide") & filters.chat(f'{CHATSTOWORK}'))
async def throwdice(client, message):
    await message.reply_text(f"{Secom}",True)
    
    
    
FunBot.run()
