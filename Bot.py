import os
import threading
from flask import Flask
import telebot
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")
print(f"TOKEN CHECK: {'FOUND' if BOT_TOKEN else 'MISSING!'}")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is Live ✅"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot is Live ✅")

def run_bot():
    bot.delete_webhook(drop_pending_updates=True)
    time.sleep(2)
    print("Bot polling started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)