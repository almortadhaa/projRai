import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# إعداد السجلات (Logs) لمراقبة عمل البوت
logging.basicConfig(level=logging.INFO)

# قراءة التوكن من متغيرات البيئة في Railway
TOKEN = os.getenv("BOT_TOKEN")

# نص الرسالة التي ستظهر للموظفين
REDIRECT_MSG = (
    "⚠️ **تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.\n\n"
    "للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل:\n"
    "👉 @GCSBook_bot\n\n"
    "نعتذر عن أي إزعاج، وشكراً لتفهمكم."
)

# دالة الرد الآلي على أي تفاعل من المستخدم
async def redirect_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(REDIRECT_MSG)

def main():
    if not TOKEN:
        print("خطأ: يرجى إضافة BOT_TOKEN في إعدادات Variables في منصة Railway.")
        return

    # إنشاء التطبيق باستخدام التوكن
    app = Application.builder().token(TOKEN).build()
    
    # التعامل مع جميع الأوامر والرسائل بنفس رد التوجيه
    app.add_handler(CommandHandler(["start", "help"], redirect_user))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, redirect_user))
    
    print("🚀 البوت يعمل الآن على Railway كبوابة توجيه...")
    app.run_polling()

if __name__ == "__main__":
    main()