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
                             "**- /dice - Throw a Dice and Give Output**\n"
                             "**- /Jokes - Gives Programming Jokes\n**"
                             "**- /decide - Send Yes or No, etc Option..**\n",True)
    
    
@FunBot.on_message(filters.command("jokes") & (filters.group | filters.private))
async def jokesop(client, message):
    SARCASM = pyjokes.get_joke()
    await message.reply_text(f"`{SARCASM}`",True)
    
    
Dechoices = ("Yes","No","Surely Yes","Maybe","Nooo.","God Knows","Cant decide","Yess","Nope")
@FunBot.on_message(filters.command("decide") & (filters.group | filters.private))
async def decideok(client, message):
    oploa = random.randrange(0,len(Dechoices)-1)
    Secom = Dechoices[oploa]
    await message.reply_text(f"{Secom}",True)
             
#@FunBot.on_message(filters.command("quote") & (filters.group | filters.private))
#async def quotes(client, message):
   #AUTHOR = random.choice(["Stephen Hawking","A._P._J._Abdul_Kalam","Vikram_Sarabhai","Narendra_Modi","Mahatma_Gandhi","Nikola_Tesla","Rabindranath_Tagore","Ruskin_Bond","Chetan_Bhagat",
   #                        "Mulk_Raj_Anand","Jawaharlal_Nehru","Chanakya","Indira_Gandhi","C._V._Raman","Kapil_Dev","Bankim_Chandra_Chattopadhyay"])
#   machine = random.choice(wikiquote.quotes(f'{AUTHOR}', lang='en')) 
# syntax = f"{machine}\n\n**Author - {AUTHOR}**" 
  # await message.reply_text(f"{syntax}",True)
    
FunBot.run()
