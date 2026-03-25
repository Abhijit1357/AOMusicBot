import asyncio
import logging
from hydrogram import filters 
from hydrogram.types import Message
from hydrogram.enums import ChatType  # <--- Yeh add kiya gaya hai

from core.client import app
from core.streamer import play_next
from core.queues import add, is_empty, clear
from core.prefetch import extract_async, prefetch

# CRITICAL: GroupCallNotFound ko yahan se hata diya gaya hai
from pytgcalls.exceptions import NoActiveGroupCall

# Logger setup
logger = logging.getLogger(__name__)

@app.on_message(filters.command(["play", "p"]))
async def play_cmd(client, message: Message):
    # Debugging: Isse aap log mein sahi enum dekh payenge
    logger.info(f"Chat Type Detected: {message.chat.type}")

    # FIXED: Hydrogram mein chat type strings nahi, Enums hote hain
    if message.chat.type not in [ChatType.GROUP, ChatType.SUPERGROUP]:
        return await message.reply("❌ **This command can only be used in a group chat.**")

    # Log incoming message
    logger.info(f"Received play command: {message.text}")

    chat_id = message.chat.id

    if len(message.command) < 2:
        return await message.reply("❌ **Usage:** /play [song name or link]")

    query = message.text.split(None, 1)[1]
    msg = await message.reply("⚡ **Processing...**")

    try:
        # Ultra fast search + extraction
        data = await extract_async(query)
    except Exception as e:
        return await msg.edit(f"❌ **Stream Error:**\n<code>{e}</code>")

    song = {
        "title": data["title"],
        "url": data["url"]
    }

    first = is_empty(chat_id)
    add(chat_id, song)

    # Next song preload logic
    asyncio.create_task(prefetch(chat_id, query))

    if first:
        try:
            await play_next(chat_id)
            await msg.edit(f"▶️ <b>Now Playing:</b> {data['title']}")
        except NoActiveGroupCall:
            clear(chat_id)
            await msg.edit("❌ **Error:** Voice Chat start karein aur Assistant ko invite karein.")
        except Exception as e:
            clear(chat_id)
            await msg.edit(f"❌ **Error:** {e}")
    else:
        await msg.edit(f"➕ <b>Queued:</b> {data['title']}")
