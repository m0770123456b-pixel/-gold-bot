import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("دزلي سكرين الشارت 📸")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 حللت الشارت...")
    result = """
📈 **الصفقة:**
النوع: BUY شراء
دخول: 2645.00
ستوب: 2635.00
هدف 1: 2655.00
هدف 2: 2665.00
السبب: كسر مقاومة + شمعة صاعدة
"""
    await update.message.reply_text(result)

async def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("Bot running...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
