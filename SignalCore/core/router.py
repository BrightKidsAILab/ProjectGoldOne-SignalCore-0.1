from core.journal import log_signal
from core.firebase_service import save_signal


def process_signal(signal):

    if not signal.valid:
        print("❌ Invalid signal.")
        return

    print("Step 1 - Logging locally...")
    log_signal(signal)
    print("💾 Signal saved.")

    print("Step 2 - Uploading to Firebase...")

    try:
        save_signal(signal)
        print("✅ Firebase upload completed.")
    except Exception as e:
        print("❌ FIREBASE ERROR")
        print(type(e).__name__)
        print(e)

    print("Step 3 - Router finished.")