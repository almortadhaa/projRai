import logging
from telegram.ext import Updater, CommandHandler

# إعداد السجلات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# نص التنبيه
MAINTENANCE_MESSAGE = """**تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.

للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل: @GCSBook_bot

نعتذر عن أي إزعاج، وشكراً لتفهمكم."""

# الدوال
def start(update, context):
    update.message.reply_text(MAINTENANCE_MESSAGE, parse_mode='Markdown')

def help_command(update, context):
    update.message.reply_text(MAINTENANCE_MESSAGE, parse_mode='Markdown')

def main():
    # التوكن يتم سحبه من متغيرات البيئة في Render لتأمين الكود
    import os
    TOKEN = os.environ.get('TOKEN')
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()