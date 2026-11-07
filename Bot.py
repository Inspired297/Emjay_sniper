import os
import telebot
from flask import Flask
import threading

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("BOT_TOKEN missing!")
    exit(1)

bot = telebot.TeleBot(BOT_TOKEN)

# Flask to satisfy Render Web Service
app = Flask(__name__)

@app.route('/')
def home():
    return "Emjay Interiors Bot is Live!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_flask, daemon=True).start()

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Emjay bot is Live ✅ Send a message!")

@bot.message_handler(func=lambda m: True)
def echo(m):
    bot.reply_to(m, f"You said: {m.text}")

print("Bot starting...")
bot.infinity_polling()
