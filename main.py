import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📸 دزلي صورة شارت الذهب وانا احللك")

async def photo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔍 جاري التحليل...")
    await update.message.reply_text(
        "📊 تحليل الشارت:\n\n"
        "1- شوف الترند: صاعد لو نازل؟\n"
        "2- حدد الدعم والمقاومة\n"
        "3- لا تدخل الا بكسر واضح\n"
        "4- الستوب 10 نقاط تحت الدعم\n"
        "5- الهدف ضعف الستوب\n\n"
        "💡 نصيحة: لا تعاكس الترند!"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.PHOTO, photo_handler))
    app.run_polling()

if __name__ == "__main__":
    main()
