import os
import telebot
from flask import Flask
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot Live!"

def run_bot():
    print("Bot polling started...")
import time
bot.delete_webhook(drop_pending_updates=True)
time.sleep(2)
    bot.infinity_polling()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot is Live ✅")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"You said: {m.text}")

# Bot in background, Flask in main so Render sees port instantly
threading.Thread(target=run_bot, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)