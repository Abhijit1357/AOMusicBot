from hydrogram import Client
from hydrogram.enums import ParseMode
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION

# Bot Client
app = Client(
    "AO_Music_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML,
    in_memory=True,
    workers=40
)

# Assistant Client
user = Client(
    "AO_User",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION,
    in_memory=True,
    workers=20
)
