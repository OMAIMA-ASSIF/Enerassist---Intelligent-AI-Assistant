import os
from motor.motor_asyncio import AsyncIOMotorClient
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)
#gère la connexion à MongoDB Atlas (via motor pour l'async).
# Replace with your actual MongoDB connection string
# Ideally, this comes from a .env file
MONGO_DETAILS = os.getenv("MONGO_URI", "mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority") 

# Add tlsAllowInvalidCertificates=True if you encounter SSL errors locally
client = AsyncIOMotorClient(MONGO_DETAILS, tlsAllowInvalidCertificates=True)
database = client.chatbot_db
user_collection = database.get_collection("users")
