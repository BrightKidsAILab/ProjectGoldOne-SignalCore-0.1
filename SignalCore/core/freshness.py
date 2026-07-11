from datetime import datetime, timedelta



def is_fresh(signal, max_age_minutes=10):
    now = datetime.utcnow()

    age = now - signal.received_at

    return age <= timedelta(minutes=max_age_minutes)

def is_fresh(signal, max_age_minutes=10):
    now = datetime.utcnow()

    age = now - signal.received_at

    return age <= timedelta(minutes=max_age_minutes)