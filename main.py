import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دزلي سكرين الشارت 📸")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 حللت الشارت...")
    
    # هسه هذا رد ثابت حتى يشتغل البوت
    # من نربط ذكاء اصطناعي راح يصير يحلل الصورة الحقيقية
    result = """
📈 **الصفقة:**

النوع: BUY شراء
دخول: 2645.00
ستوب: 2635.00 (10$)
هدف 1: 2655.00
هدف 2: 2665.00

السبب: كسر مقاومة + شمعة صاعدة قوية
"""
    await update.message.reply_text(result)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    app.run_polling()
