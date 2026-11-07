import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Emjay Interiors bot is Live! ✅")

@bot.message_handler(func=lambda m: True)
def all_msg(m):
    bot.reply_to(m, f"You said: {m.text}")

print("Bot started...")
bot.infinity_polling()
