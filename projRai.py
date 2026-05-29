import os
import asyncio
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update

# إعداد التطبيق
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
app = Flask(__name__)

# إعداد البوت
application = Application.builder().token(BOT_TOKEN).build()

# دالة الاستجابة
async def start(update: Update, context):
    await update.message.reply_text("البوت يعمل الآن بنجاح!")

application.add_handler(CommandHandler("start", start))

# مسار الـ Webhook
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
async def webhook():
    json_update = request.get_json()
    update = Update.de_json(json_update, application.bot)
    await application.process_update(update)
    return "OK", 200

# مسار للتأكد من عمل الخادم
@app.route('/')
def home():
    return "البوت يعمل بنظام Webhook"

if __name__ == "__main__":
    # تشغيل خادم Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))