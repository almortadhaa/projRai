from telegram.ext import ApplicationBuilder, CommandHandler

# التوكن الجديد
TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

async def start(update, context):
    await update.message.reply_text("مرحباً بك! أنا Mainfox أعمل الآن بنجاح.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    print("Mainfox يبدأ العمل الآن...")
    app.run_polling()