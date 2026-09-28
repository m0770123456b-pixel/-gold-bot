import os
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
    return "Bot is running"

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
    bot.send_message(message.chat.id, "⏳ جاي احلل الشارت... ثواني")
    if not OPENAI_KEY:
        bot.send_message(message.chat.id, "⚠️ المفتاح ما مضاف بعد. دزلي الشارت هنا بهاي المحادثة وانا احلله الك مجانا")
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
        r = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload, timeout=60)
        result = r.json()['choices'][0]['message']['content']
        price = get_gold_price()
        bot.send_message(message.chat.id, f"💰 السعر: ${price}\n\n📊 التحليل:\n{result}")
    except Exception as e:
        bot.send_message(message.chat.id, f"صار خطأ: {e}")

@bot.message_handler(func=lambda m: True)
def price_handler(message):
    price = get_gold_price()
    bot.send_message(message.chat.id, f"سعر الذهب: ${price}\nدزلي صورة الشارت احلله 📈")

# للتشغيل على Render
import threading
def run_bot():
    bot.infinity_polling()
threading.Thread(target=run_bot).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
