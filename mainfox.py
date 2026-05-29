from telegram.ext import ApplicationBuilder, CommandHandler

# التوكن الخاص بك
TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

async def start(update, context):
    await update.message.reply_text("مرحباً بك! أنا Mainfox. كيف يمكنني مساعدتك اليوم؟")

async def help_command(update, context):
    await update.message.reply_text("هذه قائمة الأوامر المتاحة:\n/start - لبدء المحادثة\n/help - لعرض هذه الرسالة")

async def error_handler(update, context):
    print(f"حدث خطأ: {context.error}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    
    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # إضافة معالج الأخطاء لضمان الاستمرارية
    app.add_error_handler(error_handler)
    
    print("Mainfox يعمل الآن وجاهز للأوامر...")
    app.run_polling()