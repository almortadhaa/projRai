from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

# التوكن الخاص بك
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"

# رسالة التوجيه
MAINTENANCE_TEXT = (
    "⚠️ **تنبيه هام:**\n"
    "تم إيقاف هذا البوت مؤقتاً لأغراض الصيانة والتحديث.\n\n"
    "لإتمام الاستعلام، يرجى التوجه إلى البوت البديل:\n"
    "👉 @GCSBook_bot"
)

async def redirect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MAINTENANCE_TEXT)

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاستعلام"),
        BotCommand("help", "المساعدة")
    ])

def main():
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    
    # الرد على أي أمر (start أو help أو حتى أي رسالة نصية) بالتوجيه
    app.add_handler(CommandHandler("start", redirect))
    app.add_handler(CommandHandler("help", redirect))
    
    print("🚀 البوت في وضع التوجيه الآن...")
    # استخدام run_polling مع إعدادات تقليل الحمل
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()