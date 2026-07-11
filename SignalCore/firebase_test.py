import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("config/firebase-json.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

print("Connected")

doc = db.collection("test").document()

print("Created document")

doc.set({"hello": "world"})

print("SUCCESS")