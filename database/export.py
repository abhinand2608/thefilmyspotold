import pymongo
import telegram

# Connect to the MongoDB database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Retrieve all files from the database
files = collection.find({})

# Initialize the Telegram Bot API client
bot = telegram.Bot(token='BOT_TOKEN')

# Send each file to the Telegram channel
for file in files:
    try:
        with open(file['path'], 'rb') as f:
            bot.send_document(chat_id='@yourchannel', document=f)
            print(f"File {file['path']} exported successfully.")
    except Exception as e:
        print(f"Failed to export file {file['path']}: {e}")
