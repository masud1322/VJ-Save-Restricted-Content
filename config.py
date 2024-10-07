import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17462098"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "149b3719dc136ddd05624dc69190dffd")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://realtechbd3:OMZVjlDOUiR8ODfO@cluster0.cr9m6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
