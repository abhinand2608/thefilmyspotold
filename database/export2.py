import pymongo
import telegram

# Connect to the MongoDB Atlas cluster
client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/test?retryWrites=true&w=majority")
db = client["mydatabase"]
collection = db["mycollection"]

# Retrieve all files from the database
files = collection.find({})

# Initialize the Telegram Bot API client
bot = telegram.Bot(token='YOUR_TELEGRAM_BOT_TOKEN')

# Send each file to the Telegram channel
for file in files:
    # Check that the file has a path and that it exists
    if 'path' not in file:
        print(f"File {file} is missing a path and will not be exported.")
        continue
    if not os.path.exists(file['path']):
        print(f"File {file['path']} does not exist and will not be exported.")
        continue

    # Determine the file type based on the file extension
    file_type = file['path'].split('.')[-1].lower()

    try:
        if file_type in ['mp4', 'avi', 'mkv']:
            bot.send_video(chat_id='@yourchannel', video=open(file['path'], 'rb'))
            print(f"Video {file['path']} exported successfully.")
        else:
            with open(file['path'], 'rb') as f:
                bot.send_document(chat_id='@yourchannel', document=f)
                print(f"File {file['path']} exported successfully.")
    except Exception as e:
        print(f"Failed to export file {file['path']}: {e}")

