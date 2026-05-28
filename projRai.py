import os
import logging
from threading import Thread
from flask import Flask
from telegram import Update, BotCommand
from telegram.ext import Application, CommandHandler, ContextTypes

# إعداد خادم ويب بسيط لإيهام Render بأن الخدمة نشطة
app = Flask(__name__)
@app.route('/')
def home():
    return "البوت يعمل"

def run_web():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# الكود الأصلي للبوت
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"
MAINTENANCE_TEXT = "⚠️ **تنبيه هام:**\nتم إيقاف هذا البوت مؤقتاً.\n👉 @GCSBook_bot"

async def redirect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MAINTENANCE_TEXT, parse_mode='Markdown')

def main():
    # تشغيل خادم الويب في خلفية
    Thread(target=run_web).start()
    
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", redirect))
    app.add_handler(CommandHandler("help", redirect))
    
    app.run_polling()

if __name__ == "__main__":
    main()