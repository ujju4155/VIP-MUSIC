import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VIPMUSIC import LOGGER, app, userbot
from VIPMUSIC.core.call import VIP
from VIPMUSIC.misc import sudo
from VIPMUSIC.plugins import ALL_MODULES
from VIPMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("ꜱᴛʀɪɴɢ ꜱᴇꜱꜱɪᴏɴ ɴᴏᴛ ꜰɪʟʟᴇᴅ, ᴘʟᴇᴀꜱᴇ ꜰɪʟʟᴀ ᴀ ᴘʏʀᴏɢʀᴀᴍ ᴠ2 ꜱᴇꜱꜱɪᴏɴ 😊")
        
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VIPMUSIC.plugins" + all_module)
    LOGGER("VIPMUSIC.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    await userbot.start()
    await VIP.start()
    await VIP.decorators()
    LOGGER("VIPMUSIC").info(" @aye_ujjwal "
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("VIPMUSIC").info("@aye_ujjwal")
    

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
