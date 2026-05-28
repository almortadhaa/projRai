import os
import logging
from telegram.ext import Application, CommandHandler

# إعداد السجلات لمراقبة الخطأ بالتحديد
logging.basicConfig(level=logging.INFO)

# استخدم التوكن مباشرة للتجربة (بدل os.environ) للتأكد من المشكلة
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"

async def start(update, context):
    await update.message.reply_text("البوت يعمل!")

def main():
    try:
        app = Application.builder().token(BOT_TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        print("البوت بدأ بالعمل...")
        app.run_polling()
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    main()