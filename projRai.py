import os
from flask import Flask, request
from telegram.ext import Application, CommandHandler, Update
from telegram import Update

app = Flask(__name__)
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

app_bot = Application.builder().token(BOT_TOKEN).build()

async def start(update: Update, context):
    await update.message.reply_text("البوت يعمل بنجاح!")

app_bot.add_handler(CommandHandler("start", start))

@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    # معالجة التحديثات
    return "OK", 200

@app.route('/')
def home():
    return "البوت يعمل"

# لا تضع app.run() هنا لأن gunicorn هو من سيقوم بتشغيل التطبيق