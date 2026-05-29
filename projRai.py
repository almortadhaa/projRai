import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update

app = Flask(__name__)
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

# إعداد البوت (بدون polling)
application = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("البوت يعمل الآن بنجاح عبر Webhook!")

application.add_handler(CommandHandler("start", start))

# مسار لاستقبال رسائل تيليجرام
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_update = request.get_json()
    update = Update.de_json(json_update, application.bot)
    # تشغيل المعالجة بشكل متزامن
    import asyncio
    asyncio.run(application.process_update(update))
    return "OK", 200

@app.route('/')
def home():
    return "البوت يعمل بنظام Webhook"

if __name__ == "__main__":
    # تشغيل خادم Flask فقط
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)