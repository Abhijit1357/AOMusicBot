from hydrogram import filters 
from core.client import app
from config import BOT_NAME
import logging

# Logger initialize
logger = logging.getLogger(__name__)

@app.on_message(filters.command(["start", "test"]))
async def commands_handler(client, message):
    logger.info(f"Received message: {message.text}")  # Add logging here
    chat_type = getattr(message.chat, "type", "private")
    text = message.text or ""

    # --- START ---
    if text.startswith("/start"):
            await message.reply_text(
                f"🎵 {BOT_NAME}\n\nVC Music Bot ready!\n\n"
                "• /play - Play a song\n"
                "• /pause - Pause music\n"
                "• /resume - Resume music\n"
                "• /skip - Next song\n"
                "• /stop - Stop music\n"
                "• /queue - Show queue",
                disable_web_page_preview=True
            )

    # --- TEST ---
    if text.startswith("/test"):
        await message.reply_text(f"✅ Bot is alive! Chat type: {chat_type}")
