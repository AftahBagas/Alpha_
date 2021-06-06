import asyncio
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version
from telethon import __version__, version
import platform
import sys
import time
from datetime import datetime
import psutil

from userbot import ALIVE_LOGO, ALIVE_TEKS_KUSTOM, ALIVE_NAME, CMD_HELP, StartTime, UPSTREAM_REPO_BRANCH, bot
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


modules = CMD_HELP


@ register(outgoing=True, pattern=r"^\.(?:salken)\s?(.)?")
async def amireallysalken(salken):
    user = await bot.get_me()
    await get_readable_time((time.time() - StartTime))
    await salken.edit("Halo Semuanya :)")
    await asyncio.sleep(2)
    await salken.edit("Cuma Mau Bilang")
    await asyncio.sleep(2)
    output = (
        f"`Namaku {DEFAULTUSER} Umur {USER_AGE}`\n"
        f"     `Tunggal Di {COUNTRY} Salam Kenal :)`")

CMD_HELP.update({
    "salken":
    "📚 **Cmd** : `.salken`\
    \n📄 **Descriptions** : Command Salken Untuk Dirimu :)."
})
