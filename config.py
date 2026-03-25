import os

# ========== BOT CONFIG ==========
API_ID = int(os.getenv("API_ID", "22091901"))
API_HASH = os.getenv("API_HASH", "54b0cd5fb47a40265b197f1a110b20b8")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8628889832:AAGl2wiVQiEwH1YMkFnc4R4Ys-sKUfHpK4k")
STRING_SESSION = os.getenv("STRING_SESSION", "AQFRGH0AZDBKRNad532JmrKKWjJsunU2j-cUM-ONLPdkuuVcERRXJo_1u-ahULkPzPiMvSjOIgOGbVa1OnnCmjcs1n9BXIByomrVtYTW_KzlKvCdpzl8R5g5f6W4KKIugfeZLVEmpl9KfJTtO5tSGh_dv1-K70KaXIDFA5XsShbY02XtSf5KibzTqKae_wm9t5ypzfS38CcCPPnANmSRlvRse-PGtdMTUbDfKzwQzL9mgQW9ZEl_YlrOdtd2j_FWQb4zjOFagUJ0CgaQw_qtGIBRmUsTBC-8IWkcDwiv_VYlLOp6hLFWQso2sRI0AuNNRgfXylGd6rycTT2khdZeD_1cLnZmqwAAAAH58KNUAA")

BOT_NAME = "✨Dᴀʀᴋ Aɴɢᴇʟ Music✨🤍"

# ========== SETTINGS ==========
OWNER_ID = int(os.getenv("OWNER_ID", "5390485406"))
# Yahan space hata dein "-100..." se pehle
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1003886464823"))

DOWNLOAD_DIR = "downloads"
MAX_QUEUE = 20
AUTO_LEAVE = True

# ========== STREAM (SUPER FAST CONFIG) ==========
# List ki jagah string format zyada stable hota hai kuch PyTgCalls versions mein
FFMPEG_COMMAND = (
    "-reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 "
    "-reconnect_delay_max 5 -i {input} "
    "-f s16le -ac 2 -ar 48000 -acodec pcm_s16le pipe:1"
)
