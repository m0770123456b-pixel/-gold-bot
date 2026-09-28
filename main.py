import os
import threading
import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# شغل الـ logs حتى نشوف الخطأ اذا صار
logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    print("❌ خطأ: BOT_TOKEN ما موجود!")
else:
    print(f"✅ BOT_TOKEN موجود: {TOKEN[:10]}...")

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is Alive!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("هلا! دزلي صورة الشارت 📸")

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ استلمت الصورة\nSELL من 4114 ستوپ 4125 هدف 4095")

def run_bot():
    try:
        print("🚀 جاري تشغيل البوت...")
        app = Application.builder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.PHOTO, photo))
        print("✅ البوت اشتغل وينتظر رسائل...")
        app.run_polling(drop_pending_updates=True)
    except Exception as e:
        print(f"❌ خطأ بالبوت: {e}")

if __name__ == "__main__":
    # شغل البوت بثريد منفصل
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # شغل الموقع
    port = int(os.environ.get("PORT", 10000))
    print(f"🌐 الموقع يشتغل على المنفذ {port}")
    web.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
