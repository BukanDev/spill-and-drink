# Copyright 2022 @BukanDev
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# https://github.com/BukanDev/spill-and-drink
# limitations under the License.

import os
import sys
from pyrogram import Client, filters
from random import choice
from requests import get
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL = os.environ.get("CHANNEL")
OWNER = os.environ.get("OWNER")
LOG_CHAT = os.environ.get("LOG_CHAT")

bot = Client("kontolbot",
            api_id=6,
            api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
            bot_token=BOT_TOKEN)
            
print("Bot sudah siap di gunakan")
 
# atart text
start = f"Selamat bermain dan selamat ter spill!\n\n Jangan lupa subs @{CHANNEL} dan contact @{OWNER} untuk info lainnya.\n\nNote : khusus RL bukan RP"

# spill text
spill = get("https://raw.githubusercontent.com/BukanDev/spill-and-drink/master/bahan/spill.json")

# drink
drink = get("https://raw.githubusercontent.com/BukanDev/spill-and-drink/master/bahan/drink.json")

# donasi text
donasi = f"Bagi yang punya duit penuh, atau berlebih bisa kali di transfer ke @{OWNER}"

# help text
helps = "/spill - spill dulu\n/drink - minum dulu\n/donasi - donasi ke owner bot\n/request - request spill bikinan mu"

           
@bot.on_message(filters.command("start") & filters.private & filters.group)
async def start(bot, m):
    await m.reply(start)
    
@bot.on_message(filters.command("help") & filters.private & filters.group)
async def helps(bot, m):
    await m.reply(helps)

@bot.on_message(filters.command("spill") & filters.group, group=3)
async def spill(bot, m):
    await m.reply(choice(spill))
    
@bot.on_message(filters.command("drink") & filters.group, group=3)
async def drink(bot, m):
    await m.reply_photo(choice(drink))

@bot.on_message(filters.command("donasi") & filters.group, group=3)
async def donasi(bot, m):
    await m.reply(donasi)
    
@bot.on_message(filters.command("request") & filters.group & filters.private)
async def request(bot, m):
    if len(m.command) < 2:
         return await m.reply("contoh = `/request spill photo mantan kamu`")
    mmk = m.command[1:]
    kontol = " ".join(mmk)
    await bot.copy(LOG_CHAT, message.chat.id, kontol)
    await m.reply("Terimakasih telah berkontribusi untuk kami")

bot.run()
