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
from pyrogram import Client, filters
from pyrogram.types import Message

from random import choice
from requests import get
from dotenv import load_dotenv

load_dotenv(".env")

BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
CHANNEL = os.environ.get("CHANNEL")
OWNER = os.environ.get("OWNER")
LOG_CHAT = os.environ.get("LOG_CHAT")

bot = Client("kontolbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN)
            
print("Bot sudah siap di gunakan")
# spill text
spill = get("https://raw.githubusercontent.com/BukanDev/spill-and-drink/master/bahan/spill.json").json()

# drink
drink = get("https://raw.githubusercontent.com/BukanDev/spill-and-drink/master/bahan/drink.json").json()


           
@bot.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply(f"Selamat bermain dan selamat ter spill!\n\n Jangan lupa subs @{CHANNEL} dan contact @{OWNER} untuk info lainnya.\n\nNote : khusus RL bukan RP")
    
@bot.on_message(filters.command("help"))
async def help_message(client: Client, message: Message):
    await message.reply("/spill - spill dulu\n/drink - minum dulu\n/donasi - donasi ke owner bot\n/request - request spill bikinan mu")

@bot.on_message(filters.command("spill"))
async def spill(client: Client, message: Message):
    await message.reply_text(choice(spill))
    
@bot.on_message(filters.command("drink"))
async def drink(client: Client, message: Message):
    await message.reply_photo(choice(drink))

@bot.on_message(filters.command("donasi"))
async def donasi(client: Client, message: Message):
    await message.reply(f"Bagi yang punya duit penuh, atau berlebih bisa kali di transfer ke @{OWNER}")
    
@bot.on_message(filters.command("request"))
async def request(client: Client, message: Message):
    if len(message.command) < 2:
         return await message.reply("contoh = `/request spill photo mantan kamu`")
    mmk = message.command[1:]
    kontol = " ".join(mmk)
    await bot.send_message(LOG_CHAT, f"{message.from_user.mention}\nPesan: {kontol}")
    await message.reply("Terimakasih telah berkontribusi untuk kami")
    
    

bot.run()
