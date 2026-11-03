import telebot, os
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
YOUR_ID = 5119935507

@bot.message_handler(commands=['start'])
def s(m):
 bot.reply_to(m, "🏠 EMJAY INTERIORS\nWestlands & Kileleshwa\nSend job e.g. Kileleshwa painting")

@bot.message_handler(func=lambda x: True)
def h(m):
 if m.chat.id==YOUR_ID:
  bot.send_message(YOUR_ID, f"Lead saved: {m.text[:200]}")
 else:
  bot.send_message(YOUR_ID, f"🔥 CLIENT {m.from_user.first_name}: {m.text} ID:{m.chat.id}")
  bot.reply_to(m, "Thanks! Emjay Interiors will call in 30 mins. Assessment 1k.")

bot.infinity_polling()
