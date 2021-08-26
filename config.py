import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴄʏʙᴇʀ ᴍᴜsɪᴄ ʙᴏᴛ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/cd0b87484429704c7b935.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/91034f175d41040d45b38.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/c8a0e9c544c5ea689caf9.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "CyberMusikBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "SaitamaHelper")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "CyberSupportGroup")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "CyberMusicProject")
OWNER_NAME = getenv("OWNER_NAME", "Badboyanim") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Badboyanim")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "250"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
