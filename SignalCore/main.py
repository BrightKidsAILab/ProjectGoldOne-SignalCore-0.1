import firebase_admin
from firebase_admin import credentials

from telegram.listener import start_listener


def initialize_firebase():
    try:
        cred = credentials.Certificate("config/firebase-json.json")
        firebase_admin.initialize_app(cred)
        print("✅ Firebase initialized successfully.")
    except Exception as e:
        print(f"❌ Firebase initialization failed: {e}")


def main():
    print("=" * 50)
    print("ProjectGoldOne SignalCore")
    print("Starting Telegram Listener...")
    print("=" * 50)

    initialize_firebase()

    start_listener()


if __name__ == "__main__":
    main()