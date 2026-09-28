import os, threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
web = Flask(__name__)

@web.route("/")
def home(): return "ok"

async def start(update, context):
    await update.message.reply_text("هلا! دزلي صورة الشارت 📸")

async def photo(update, context):
    await update.message.reply_text("✅ استلمت الصورة\nSELL من 4114 ستوپ 4125 هدف 4095")

def run():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, photo))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run).start()
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
