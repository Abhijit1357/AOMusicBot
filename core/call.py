from pytgcalls import PyTgCalls
from pytgcalls.types import StreamEnded
from core.client import user
from core.queues import pop, is_empty
from core.streamer import play_next  # Ensure this import is correct for your play_next function

# Assistant client ko use karke PyTgCalls initialize karein
call_py = PyTgCalls(user)

# Event handler for when updates (like stream ending) occur
@call_py.on_update()
async def handler(client, update):
    # Jab gaana khatam ho jaye (StreamEnded event)
    if isinstance(update, StreamEnded):
        chat_id = update.chat_id
        print(f"Stream ended for chat {chat_id}")
        
        # Queue se purana gaana hatao
        pop(chat_id)
        print(f"Song removed from queue for chat {chat_id}")

        # Check karo agar queue mein aur gane hain
        if not is_empty(chat_id):
            try:
                print(f"Playing next song in the queue for chat {chat_id}")
                await play_next(chat_id)  # Ensure play_next handles the actual streaming logic
            except Exception as e:
                print(f"Error playing next song for chat {chat_id}: {e}")
        else:
            try:
                print(f"Queue is empty, leaving call for chat {chat_id}")
                # Agar queue khaali hai toh call leave kar do
                await client.leave_call(chat_id)
            except Exception as e:
                print(f"Error leaving call for chat {chat_id}: {e}")

# Start PyTgCalls for managing calls (if not started earlier)
async def start_call_py():
    try:
        await call_py.start()  # Start the PyTgCalls instance
        print("PyTgCalls started successfully.")
    except Exception as e:
        print(f"Error starting PyTgCalls: {e}")
