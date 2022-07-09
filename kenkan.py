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
SPILL = [
 "Spill makanan yang belum pernah lu makan sama sekali",
 "spill yang paling ngeselin",
 "Spill lagu indo fav",
 "Spill orang yang bikin kamu terkesima setiap saat",
 "Spill mantan cp kamu",
 "spill rc telegram",
 "spill kelakukan paling memalukan pas masih kecil",
 "Spil Adek kelas yg ganteng",
 "spill kenapa kamu selalu ngedahuluin orang lain daripada diri kamu sendiri?",
 "spill kejadian memalukan",
 "siapa yg sering ngajak gelud?",
 "Spill pengalaman terhoror",
 "spill kang ghosting",
 "spill nama org org tersayang",
 "Spill orang yang pernah bully lu!",
 "spill chat terakhir kali sama mantan",
 "Pengalaman teraneh",
 "spill siapa org yang paling lu benci di gc",
 "Spill pernah jadian sama kating?",
 "spill chat waktu lu diputusin",
 "Spill menunggu atau menanti?",
 "spesial song buat seseorang? spill ke gc dan tag orangnya !",
 "Spill alamat rumah",
 "Spill tentang mantan",
 "spill nama panggilan klian disekolah",
 "spill orang terjamet",
 "Sebutin film/drama/series/anime yang jadi fav kamu",
 "spill hal yang dikangenin dari mantan",
 "spill warna rambut yang pengen dicoba",
 "spill orang yg paling ditakuti buat pergi",
 "spill tukang boong",
 "Spill hal yang lagi lo pikirin sekarang",
 "spill theme telegram",
 "spill nama depan org yg lagi lu sukain sekarang",
 "Spill yang selalu bikin kamu gemes dengan kelakuannya",
 "spiil id tik tok lu",
 "Sapa, orang yang paling berkesan pas kelas 6 SD??",
 "spill orang paling dongo",
 "spill kelakuan cp yang suka bikin cemburu",
 "spill crush yg ga peka²",
]

# drink
DRINK = [
 "https://telegra.ph/file/138625bd10764fb4a095f.jpg",
 "https://telegra.ph/file/131957d3e688441cc9b3f.jpg",
 "https://telegra.ph/file/62a9e59207d711400868a.jpg",
 "https://telegra.ph/file/2dfe5ebf60541e17ff2fe.jpg",
 "https://telegra.ph/file/cf99b72ae0d5b543c465b.jpg",
]



           
@bot.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply(f"Selamat bermain dan selamat ter spill!\n\n Jangan lupa subs @{CHANNEL} dan contact @{OWNER} untuk info lainnya.\n\nNote : khusus RL bukan RP")
    
@bot.on_message(filters.command("help"))
async def help_message(client: Client, message: Message):
    await message.reply("/spill - spill dulu\n/drink - minum dulu\n/donasi - donasi ke owner bot\n/request - request spill bikinan mu")

@bot.on_message(filters.command("spill"))
async def spill(client: Client, message: Message):
    await message.reply(choice(SPILL))
    
@bot.on_message(filters.command("drink"))
async def drink(client: Client, message: Message):
    await message.reply_photo(choice(DRINK))

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
