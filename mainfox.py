from telegram.ext import ApplicationBuilder, CommandHandler
from flask import Flask
import threading
import os

# 1. إعداد خادم ويب بسيط لـ Render
app = Flask(__name__)
@app.route('/')
def home():
    return "Mainfox is running 24/7!"

def run_web_server():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# 2. كود البوت
async def start(update, context):
    await update.message.reply_text("مرحباً! أنا Mainfox أعمل 24/7.")

async def help_command(update, context):
    await update.message.reply_text("الأوامر: /start , /help")

if __name__ == "__main__":
    # تشغيل خادم الويب في خلفية منفصلة
    threading.Thread(target=run_web_server, daemon=True).start()
    
    TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CommandHandler("help", help_command))
    
    print("Mainfox يعمل الآن مع خادم ويب للصمود 24/7...")
    app_bot.run_polling()