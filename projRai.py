import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update
import asyncio

# التوكن الجديد المعتمد
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
app = Flask(__name__)

# تهيئة البوت
bot_app = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("البوت يعمل الآن بنظام Webhook بنجاح!")

bot_app.add_handler(CommandHandler("start", start))

# دالة الـ Webhook المباشرة
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data:
        update = Update.de_json(json_data, bot_app.bot)
        # تنفيذ التحديث بشكل غير متزامن
        asyncio.run(bot_app.process_update(update))
        return "OK", 200
    return "Invalid Request", 400

@app.route('/')
def index():
    return "البوت يعمل."

if __name__ == "__main__":
    # تشغيل الخادم
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)