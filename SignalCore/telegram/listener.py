from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

from parser.signal_parser import parse_signal
from filters.validator import validate_signal
from core.normalizer import normalize
from core.deduplicator import is_duplicate
from core.freshness import is_fresh
from core.channel_manager import get_channel
from core.router import process_signal

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

        print("\n" + "=" * 60)
        print("NEW TELEGRAM MESSAGE")
        print("=" * 60)

        print(event.raw_text)

        channel = get_channel(event)

        parsed = parse_signal(event.raw_text)

        signal = normalize(parsed)

        signal.source = channel.channel_name or "Saved Messages"

        signal = validate_signal(signal)

        channel.record_signal(signal.confidence)

        print("\nValidated Signal")
        print(signal)

        print("\nChannel Statistics")
        print(f"Source             : {signal.source}")
        print(f"Signals Processed  : {channel.total_signals}")
        print(f"Average Confidence : {channel.average_confidence:.2f}%")
        print(f"Reliability        : {channel.reliability:.2f}%")

        if not is_fresh(signal):
            print("\n⚠ Signal expired.")
            print("=" * 60)
            return

        if is_duplicate(signal):
            print("\n⚠ Duplicate signal ignored.")
            print("=" * 60)
            return

        process_signal(signal)

        print("=" * 60)

    client.start()

    print("Telegram listener started successfully.")
    print("Waiting for incoming trading signals...")

    client.run_until_disconnected()