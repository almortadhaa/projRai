import logging
from telegram.ext import Updater, CommandHandler

# إعداد السجلات لمراقبة الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# نص التنبيه الموحد
MAINTENANCE_MESSAGE = """**تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.

للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل: @GCSBook_bot

نعتذر عن أي إزعاج، وشكراً لتفهمكم."""

# دالة التعامل مع الأوامر
def start(update, context):
    update.message.reply_text(MAINTENANCE_MESSAGE, parse_mode='Markdown')

def help_command(update, context):
    update.message.reply_text(MAINTENANCE_MESSAGE, parse_mode='Markdown')

def main():
    # ضع التوكن الخاص بك هنا أو استخدم متغير بيئة
    TOKEN = 'YOUR_BOT_TOKEN_HERE' 
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # إضافة الأوامر
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # بدء تشغيل البوت
    updater.start_polling()
    
    # هذا السطر يمنع البوت من الإغلاق فوراً ويجعله ينتظر الأوامر
    updater.idle()

if __name__ == '__main__':
    main()