import firebase_admin
from firebase_admin import credentials, firestore


cred = credentials.Certificate("projeto-sd-856ba-firebase-adminsdk-fbsvc-ce5f94f2df.json")
firebase_admin.initialize_app(cred)

# Conectar ao Firestore
db = firestore.client()
