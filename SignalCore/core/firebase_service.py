from firebase_admin import firestore
import traceback


def save_signal(signal):
    db = firestore.client()

    data = {
        "pair": signal.pair,
        "direction": signal.direction,
        "entry": signal.entry,
        "stop_loss": signal.stop_loss,
        "take_profits": signal.take_profits,
        "confidence": signal.confidence,
        "risk_reward": signal.risk_reward,
        "source": signal.source,
        "valid": signal.valid,
        "errors": signal.errors,
        "received_at": signal.received_at.isoformat(),
    }

    print("Creating document...")

    doc = db.collection("signals").document()

    print("Document ID:", doc.id)

    print("About to call doc.set()")

    try:
        doc.set(data)
        print("doc.set() returned successfully")
        print("☁ Signal uploaded to Firebase.")
    except Exception:
        print("Exception inside doc.set():")
        traceback.print_exc()