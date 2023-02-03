import pymongo
import telegram

# Connect to the MongoDB Atlas cluster
uri = "mongodb+srv://<username>:<password>@cluster.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client["mydatabase"]
collection = db["mycollection"]

# Retrieve all files from the database
files = collection.find({})

# Initialize the Telegram Bot API client
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# Send each file to the Telegram channel
for file in files:
    try:
        with open(file['path'], 'rb') as f:
            bot.send_document(chat_id='@yourchannel', document=f)
            print(f"File {file['path']} exported successfully.")
    except Exception as e:
        print(f"Failed to export file {file['path']}: {e}")
