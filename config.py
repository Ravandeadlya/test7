import os
API_ID :int = int(os.environ.get("API_ID", "20554523"))
API_HASH :str = os.environ.get("API_HASH", "b59b15516da5318bc1d7f80880ffe8a1")
BOT_TOKEN :str= os.environ.get("BOT_TOKEN", "7479400988:AAFwlonjSMYJiyq4GZRQZh6aOLUZ0XMrTeo")
UPDATE_CHNL :str = os.environ.get("UPDATE_CHNL", "totote_min")
SUPPORT_GRP :str = os.environ.get("SUPPORT_GRP", "totote_min")
START_IMG :str = os.environ.get(
    "START_IMG", "https://telegra.ph/file/f95a2ad0069f7ffaf6b02.jpg"
)

MONGO_DB_URI :str = os.environ.get(
    "MONGO_DB_URI",
    "mongodb+srv://Sgygd:Sgygd@cluster0.kx1hp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
OWNER_ID :int= os.environ.get("OWNER_ID", 6448259089)

