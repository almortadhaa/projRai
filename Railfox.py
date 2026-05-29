import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update
import asyncio

# التوكن الجديد
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
app = Flask(__name__)

# إعداد البوت (بدون تشغيل أي polling)
bot_app = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Railfox يعمل الآن بنظام Webhook!")

bot_app.add_handler(CommandHandler("start", start))

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    # استلام التحديث من تيليجرام
    json_data = request.get_json()
    update = Update.de_json(json_data, bot_app.bot)
    
    # معالجة التحديث
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot_app.process_update(update))
    
    return "OK", 200

@app.route('/')
def home():
    return "Railfox Online"

if __name__ == "__main__":
    # تشغيل خادم Flask
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))