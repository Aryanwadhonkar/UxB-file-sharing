#(©)CodeXBotz
#By @Codeflix_Bots



import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7795049936:AAEqf58MqPhd0uPRoXzjSm4Su1MRiJO7k7c")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24103884"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "257516f22417652d03896cb2e007d6df")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002348593955"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1672634667"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Wleakshere:Thunderstrikes27@wleakshere.api7w.mongodb.net/?retryWrites=true&w=majority&appName=Wleakshere")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster01")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002435180530"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "0"))
FORCESUB_CHANNEL3 = int(os.environ.get("FORCESUB_CHANNEL3", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#token varibles
# my shortner https://dashboard.shareus.io/signup/lifetime/U9AZbV

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "seturl.in")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "9a256c2ecb6c16539243b96e410602df1e1d3674")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","gojfsi/2")

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Nya~! {first} It’s a pleasure to see you! Let’s enjoy this moment together!</b>")
try:
    ADMINS=[6695586027]
    for x in (os.environ.get("ADMINS", "1672634667").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Um,~! {first} <b>If you could please join the channel first, then I’ll be all yours to take care of~! ✨</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @wleakshere</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ !"

ADMINS.append(OWNER_ID)
ADMINS.append(1672634667)

LOG_FILE_NAME = "wleakshere.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
