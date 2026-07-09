from telethon import TelegramClient, events
from dotenv import load_dotenv

import os

from parser.signal_parser import parse_signal

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = os.getenv("SESSION_NAME")

client = TelegramClient(
    SESSION_NAME,
    API_ID,
    API_HASH
)


def start_listener():

    @client.on(events.NewMessage)
    async def handler(event):

        print("\n============================")
        print("NEW TELEGRAM MESSAGE")
        print("============================")

        print(event.raw_text)

        parsed = parse_signal(event.raw_text)

        print("\nParsed Signal")

        print(parsed)

    client.start()

    print("Telegram listener started successfully.")
    print("Waiting for incoming trading signals...")

    client.run_until_disconnected()