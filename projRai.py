import os
import logging
from threading import Thread
from flask import Flask
from telegram.ext import Application, CommandHandler
from telegram import BotCommand

# إعداد خادم ويب للبقاء على قيد الحياة
app = Flask(__name__)
@app.route('/')
def home():
    return "البوت يعمل"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# التوكن الجديد (ضع التوكن الذي حصلت عليه بعد Revoke)
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"

async def start(update, context):
    await update.message.reply_text("البوت يعمل بنجاح!")

def main():
    # تشغيل الخادم
    Thread(target=run_web, daemon=True).start()
    
    # إعداد البوت مع زيادة مهلة الاتصال (Connect Timeout)
    app = Application.builder().token(BOT_TOKEN).connect_timeout(30).read_timeout(30).build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("🚀 البوت يحاول الاتصال بتيليجرام...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()