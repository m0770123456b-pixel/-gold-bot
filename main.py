import os
import threading
from flask import Flask
import telebot
import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running"

def get_gold_price():
    try:
        # سعر الذهب العالمي
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
        return f"{r['price']:.2f} $"
    except:
        return "غير متوفر حاليا"

@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "اهلا بيك ببوت الذهب 💰\nدز /gold لمعرفة السعر")

@bot.message_handler(commands=['gold'])
def gold(m):
    price = get_gold_price()
    bot.send_message(m.chat.id, f"💰 سعر اونصة الذهب الان: {price}")

def run_flask():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    print("Bot started...")
    bot.infinity_polling()
