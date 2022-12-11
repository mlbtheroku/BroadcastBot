import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5861946623:AAGgy4F6sqLIs8FCzjNqN4ppgknw_2gvBRU")
API_ID = int(os.environ.get("API_ID", "17894641"))
API_HASH = os.environ.get("API_HASH", "4e5b39e5c7c6066e5144dfc50cf466cf")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001705637043"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5468192421").split())
DB_URL = os.environ.get("DB_URL", "mongodb+srv://testorg:testorg@cluster0.0menx0b.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
