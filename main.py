import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("دزلي سكرين الشارت 📸")

def handle_photo(update, context):
    update.message.reply_text("🔍 جاي احلل...")
    txt = """
📈 **الصفقة:**
النوع: BUY شراء
دخول: 2645.00
ستوب: 2635.00
هدف1: 2655.00
هدف2: 2665.00
"""
    update.message.reply_text(txt)

updater = Updater(BOT_TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))

print("Bot running...")
updater.start_polling()
updater.idle()
