import os
import uuid
import shutil
import logging
import random
import asyncio as shh
import pyjokes
import wikiquote
from pyrogram import Client, filters
from creds import Credentials
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config
logging.basicConfig(level=logging.INFO)


FunBot = Client(
    "Fun Robot",
    bot_token=Credentials.BOT_TOKEN,
    api_id=Credentials.API_ID,
    api_hash=Credentials.API_HASH,
)

CHATSTOWORK = Credentials.CHAT_GROUPS
OWNERID = Config.OWNER_ID

@FunBot.on_message(filters.command("start") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def start(client, message):
    await message.reply_text(
        f"**Hi, I am FunBot. I can Perform Many Task For You. To know then send `/help`**",
        True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Updates Channel", url="t.me/prothinkergang")],
                [InlineKeyboardButton(text="Deploy Your Own Bot",url="https://github.com/ProThinkerGang/FunRobot")]
            ]
        )
    )

   
@FunBot.on_message(filters.command("dice") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def throwdice(client, message):
    diceoutput = random.randrange(1,6)
    await message.reply_text(f"**Results ==>> {diceoutput}**",True)
    
@FunBot.on_message(filters.command("help") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def helpcmd(client, message):
    await message.reply_text(f"**Below are The Avaliable Commands**\n\n"
                             "-`/dice`- Throw a Dice and Give Output\n"
                             "-`/Jokes`- Gives Programming Jokes\n"
                             "-`/decide`- Send Yes or No, etc Option..\n"
                             "-`/quote`- send a Quote of Stephen Hawking",True)
    
@FunBot.on_message(filters.command("jokes") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def jokesop(client, message):
    SARCASM = pyjokes.get_joke()
    await message.reply_text(f"`{SARCASM}`",True)
    
    
Dechoices = ("Yes","No","Surely Yes","Maybe","Nooo.","God Knows","Cant decide")
@FunBot.on_message(filters.command("decide") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def decideok(client, message):
    oploa = random.randrange(0,len(Dechoices)-1)
    Secom = Dechoices[oploa]
    await message.reply_text(f"{Secom}",True)
  
@FunBot.on_message(filters.command("quote") & (filters.chat(f'{CHATSTOWORK}') | filters.user(f"{OWNERID}")))
async def quotes(client, message):
    oze = random.choice(wikiquote.quotes('stephen Hawking', lang="en"))
    await message.reply_text(f"{oze}",True)
    
FunBot.run()
