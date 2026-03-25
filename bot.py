import asyncio
import logging
import os
import importlib
from hydrogram import idle

# --- PyTgCalls fix ---
import hydrogram
import sys
sys.modules["pyrogram"] = hydrogram

from core.client import app, user
from core.call import call_py
from config import BOT_NAME

# Logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AO_Music")

# --- Plugin Loader ---
def load_plugins():
    plugins_dir = "plugins"
    if not os.path.exists(plugins_dir):
        logger.error("❌ plugins folder not found!")
        return

    for file in os.listdir(plugins_dir):
        if file.endswith(".py") and not file.startswith("__"):
            module = f"{plugins_dir}.{file[:-3]}"
            try:
                importlib.import_module(module)
                logger.info(f"✅ Loaded: {module}")
            except Exception as e:
                logger.error(f"❌ Failed: {module} → {e}")

# --- MAIN ---
async def main():
    print("Bot is starting...")  # Debug print to check if main is being executed.
    try:
        print("Starting bot client...")
        await app.start()
        logger.info("✅ Bot Started")
        print("Bot connected!")

        me = await app.get_me()
        print(f"\n🤖 RUNNING BOT: @{me.username} | {me.first_name} | IS_BOT: {me.is_bot}\n")

        load_plugins()

        print("Starting assistant client...")
        await user.start()
        logger.info("✅ Assistant Started")
        print("Assistant connected!")

        print("Starting PyTgCalls...")
        await call_py.start()
        logger.info("✅ PyTgCalls Started")
        print("PyTgCalls connected!")

        print("\n🔥 BOT ONLINE — /start ya /test bhejo\n")
        await idle()

    except Exception as e:
        logger.error(f"❌ Fatal Error: {e}")
        print(f"❌ Fatal Error: {e}")  # Print the error in terminal

    finally:
        if getattr(app, "is_connected", False):
            await app.stop()
        if getattr(user, "is_connected", False):
            await user.stop()
        logger.info("❌ Bot Stopped")
        print("❌ Bot Stopped")

# --- RUN MAIN ---
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())  # Start the event loop properly
        print("Event loop finished...")
    except Exception as e:
        print(f"Error starting event loop: {e}")
