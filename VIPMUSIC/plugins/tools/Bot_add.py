import random
from pyrogram import Client
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InputMediaVideo, Message
from config import LOGGER_ID as LOG_GROUP_ID
from VIPMUSIC import app  
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.utils.database import delete_served_chat
from VIPMUSIC.utils.database import get_assistant
TEST_ID = int("-1002037873412")


photo = [
    "https://t.me/mmaminhindi/2305"
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                count = await app.get_chat_members_count(chat.id)
                username = message.chat.username if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐆ʀᴏᴜᴘ"
                msg = (
                    f"**ᴍᴜꜱɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ #ɴᴇᴡ_ɢʀᴏᴜᴘ**\n\n"
                    f"**ᴄʜᴀᴛ ɴᴀᴍᴇ:** {message.chat.title}\n"
                    f"**ᴄʜᴀᴛ ɪᴅ:** {message.chat.id}\n"
                    f"**ᴄʜᴀᴛ ᴜꜱᴇʀɴᴀᴍᴇ:** @{username}\n"
                    f"**ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀꜱ:** {count}\n"
                    f"**ᴀᴅᴅᴇᴅ ʙʏ:** {message.from_user.mention}"
                )
                await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"ᴀᴅᴅᴇᴅ ʙʏ", url=f"tg://openmessage?user_id={message.from_user.id}")]
             ]))
                await userbot.join_chat(f"{username}")
    except Exception as e:
        print(f"Error: {e}")
        

@app.on_message(filters.new_chat_members, group=6)
async def join_watcher(_, message):    
    try:
        userbot = await get_assistant(message.chat.id)
        chat = message.chat
        for members in message.new_chat_members:
            if members.id == app.id:
                await userbot.join_chat("dhhdshhss6")
                await userbot.send_photo(TEST_ID, photo=random.choice(photo), caption=f"@{app.username}")
                await userbot.leave_chat(TEST_ID)
    except Exception as e:
        print(f"Error: {e}")
        
