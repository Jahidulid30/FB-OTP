from telethon import TelegramClient, events
from config import API_ID, API_HASH, PHONE, SOURCE_GROUPS, TARGET_GROUP

client = TelegramClient("otp_forwarder", API_ID, API_HASH)

@client.on(events.NewMessage(chats=[int(g) for g in SOURCE_GROUPS]))
async def handler(event):
    try:
        await client.send_message(TARGET_GROUP, event.message)
        print(f"Forwarded message from {event.chat_id}")
    except Exception as e:
        print(f"Error: {e}")

async def main():
    await client.start(PHONE)
    print("Bot is running...")
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())
