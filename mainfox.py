from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading
import os

# إعداد خادم ويب بسيط للصمود 24/7
app = Flask(__name__)
@app.route('/')
def home():
    return "Mainfox is running 24/7!"

def run_web_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# رسالة التنبيه الموحدة
ALERT_MESSAGE = (
    "**تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.\n\n"
    "للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل: @GCSBook_bot\n\n"
    "نعتذر عن أي إزعاج، وشكراً لتفهمكم."
)

async def alert_command(update, context):
    await update.message.reply_text(ALERT_MESSAGE, parse_mode="Markdown")

if __name__ == "__main__":
    # تشغيل خادم الويب
    threading.Thread(target=run_web_server, daemon=True).start()
    
    TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
    app_bot = ApplicationBuilder().token(TOKEN).build()
    
    # ربط الأوامر برسالة التنبيه
    app_bot.add_handler(CommandHandler("start", alert_command))
    app_bot.add_handler(CommandHandler("help", alert_command))
    
    print("Mainfox يعمل الآن مع رسالة التنبيه...")
    app_bot.run_polling()