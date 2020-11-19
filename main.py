import os
import uuid
import shutil
import logging
import random
import asyncio as shh
import wikiquote
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

@FunBot.on_message(filters.command("start") & (filters.group | filters.private))
async def start(client, message):
    await message.reply_text(
        f"**Hi, I am FunBot. I can Perform Many Task For You. To know then send `/help`**",
        True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton(text="Updates Channel", url="t.me/prothinkergang")],
                [InlineKeyboardButton(text="Deploy Your Own Bot",url="https://dashboard.heroku.com/new?template=https://github.com/prothinkergang/funrobot")]
            ]
        )
    )

   
@FunBot.on_message(filters.command("dice") & (filters.group | filters.private))
async def throwdice(client, message):
    diceoutput = random.randrange(1,6)
    await message.reply_text(f"**Results ==>> {diceoutput}**",True)
    
@FunBot.on_message(filters.command("help") &  (filters.group | filters.private)
                  )
async def helpcmd(client, message):
    await message.reply_text(f"**Below are The Avaliable Commands**\n\n"
                             "-`/dice`- Throw a Dice and Give Output\n"
                             "-`/Jokes`- Gives Programming Jokes\n"
                             "-`/decide`- Send Yes or No, etc Option..\n"
                             "-`/quote`- send a Quote",True)
    
    
@FunBot.on_message(filters.command("jokes") & (filters.group | filters.private))
async def jokesop(client, message):
    SARCASM = pyjokes.get_joke()
    await message.reply_text(f"`{SARCASM}`",True)
    
    
Dechoices = ("Yes","No","Surely Yes","Maybe","Nooo.","God Knows","Cant decide")
@FunBot.on_message(filters.command("decide") & (filters.group | filters.private))
async def decideok(client, message):
    oploa = random.randrange(0,len(Dechoices)-1)
    Secom = Dechoices[oploa]
    await message.reply_text(f"{Secom}",True)
             
@FunBot.on_message(filters.command("quote") & (filters.group | filters.private))
async def quotes(client, message):
    abc = random.choice(wikiquote.quotes('Stephen Hawking', lang="en"))
    abc1 = f"{abc}\n\n**Author - __Stephen Hawking__**"
    bcd = random.choice(wikiquote.quotes('APJ Abdul Kalam', lang="en"))
    bcd1 = f"{bcd}\n\n**Author - __Apj Abdul Kalam__**"
    allen = random.choice([abc1,bcd1])
    await message.reply_text(f"{allen}",True)
    
FunBot.run()
