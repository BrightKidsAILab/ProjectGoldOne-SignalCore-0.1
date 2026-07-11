import os
import firebase_admin
from firebase_admin import credentials

_initialized = False


def initialize_firebase():
    """
    Initializes Firebase once.
    Safe to call multiple times.
    """

    global _initialized

    if _initialized:
        return True

    try:

        json_file = os.getenv("FIREBASE_CREDENTIALS")

        if not json_file:
            print("⚠ FIREBASE_CREDENTIALS not found in .env")
            return False

        if not os.path.exists(json_file):
            print(f"⚠ Firebase credential file not found: {json_file}")
            return False

        cred = credentials.Certificate(json_file)

        firebase_admin.initialize_app(cred)

        _initialized = True

        print("✅ Firebase initialized successfully.")

        return True

    except ValueError:
        # Firebase already initialized
        _initialized = True
        return True

    except Exception as e:

        print("❌ Firebase initialization failed.")
        print(e)

        return False