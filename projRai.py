import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler, Update
from telegram import Update

app = Flask(__name__)
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"

# إعداد البوت
app_bot = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("البوت يعمل بنجاح عبر Webhook!")

app_bot.add_handler(CommandHandler("start", start))

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_update = request.get_json()
    update = Update.de_json(json_update, app_bot.bot)
    app_bot.update_queue.put(update)
    return "OK", 200

@app.route('/')
def home():
    return "البوت يعمل بنظام Webhook"

if __name__ == "__main__":
    # ملاحظة: في Render، يجب ضبط Webhook URL عبر API تيليجرام
    # يمكنك وضع رابط تطبيقك هنا: https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://<YOUR_APP_NAME>.onrender.com/<TOKEN>
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)