import os
import threading
from flask import Flask
import telebot
from telebot import types
import time

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Emjay Sniper Bot is Live ✅"

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("📊 Help", callback_data="help")
    btn2 = types.InlineKeyboardButton("ℹ️ About", callback_data="about")
    markup.add(btn1, btn2)
    
    text = f"""
🔥 *Welcome to Emjay Sniper* 🔥

Hello {message.from_user.first_name}!

✅ Bot is Live & Ready

📌 *Available Commands:*
/start - Restart bot
/help - How to use
/about - About us

Click below 👇
"""
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.reply_to(message, "🆘 *Help*\n\nJust send /start to use the bot.\nSupport: @YourUsername", parse_mode="Markdown")

@bot.message_handler(commands=['about'])
def about_cmd(message):
    bot.reply_to(message, "🔥 *Emjay Sniper*\n\nFast, secure & reliable.\nBuilt with ❤️", parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "help":
        help_cmd(call.message)
    elif call.data == "about":
        about_cmd(call.message)

def run_bot():
    bot.delete_webhook(drop_pending_updates=True)
    time.sleep(2)
    print("Bot polling started...")
    bot.infinity_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)