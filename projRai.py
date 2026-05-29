import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update

app = Flask(__name__)
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

# إعداد البوت
application = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("البوت يعمل بنجاح عبر Webhook!")

application.add_handler(CommandHandler("start", start))

# مسار الويب لاستقبال تحديثات تيليجرام
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    # تمرير التحديثات للبوت
    update = Update.de_json(request.get_json(), application.bot)
    application.bot.process_update(update)
    return "OK", 200

@app.route('/')
def home():
    return "البوت يعمل بنظام Webhook"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))