import os
import threading
from flask import Flask
import telebot
import requests
import base64

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
bot = telebot.TeleBot(BOT_TOKEN)

app = Flask(__name__)
@app.route('/')
def home():
    return "Bot is running - Analyzer mode"

def get_gold_price():
    try:
        r = requests.get("https://api.gold-api.com/price/XAU", timeout=10).json()
        return f"{r['price']:.2f}"
    except:
        return "غير متوفر"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "هلا بيك حبيبي 👋\nدزلي سكرين للشارت وانا احلله الك بيع لو شراء 📈")

@bot.message_handler(content_types=['photo'])
def analyze(message):
    bot.reply_to(message, "⏳ جاي احلل الشارت... ثواني")
    if not OPENAI_KEY:
        bot.reply_to(message, "⚠️ لازم تضيف OPENAI_KEY في Render")
        return
    try:
        file_info = bot.get_file(message.photo[-1].file_id)
        file_url = f"https://api.telegram.org/file/bot{BOT_TOKEN}/{file_info.file_path}"
        photo_bytes = requests.get(file_url).content
        b64 = base64.b64encode(photo_bytes).decode('utf-8')
        headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
        payload = {
            "model": "gpt-4o",
            "messages": [{
                "role": "user",
                "content": [
                    {"type": "text", "text": "انت محلل فني محترف للذهب XAUUSD. حلل الشارت: حدد الترند، الدعم والمقاومة، وهل بيع او شراء مع الستوب والهدف. جاوب بالعراقي مختصر"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{b64}"}}
                ]
            }],
            "max_tokens": 600
        }
        r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers,
