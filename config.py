import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "17462098"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "149b3719dc136ddd05624dc69190dffd")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://lelej78399:8uH6Z0GYhX9sizXp@cluster0.zymda.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
