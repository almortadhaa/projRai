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
    return "البوت يعمل الآن"

def run_web():
    # استخدام المنفذ الذي تحدده منصة Render
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# التوكن الخاص بك
BOT_TOKEN = "8404596881:AAELutS84xKY33Vk_BFrG-Fgxmt9YjbiXxA"

# رسالة التوجيه
MAINTENANCE_TEXT = (
    "⚠️ **تنبيه هام:**\n"
    "تم إيقاف هذا البوت مؤقتاً لأغراض الصيانة والتحديث.\n\n"
    "لإتمام الاستعلام، يرجى التوجه إلى البوت البديل:\n"
    "👉 @GCSBook_bot"
)

async def redirect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MAINTENANCE_TEXT, parse_mode='Markdown')

async def post_init(application: Application):
    await application.bot.set_my_commands([
        BotCommand("start", "بدء الاستعلام"),
        BotCommand("help", "المساعدة")
    ])

def main():
    # تشغيل خادم الويب في خيط منفصل (Thread)
    Thread(target=run_web).start()
    
    # إعداد البوت
    app = Application.builder().token(BOT_TOKEN).post_init(post_init).build()
    
    app.add_handler(CommandHandler("start", redirect))
    app.add_handler(CommandHandler("help", redirect))
    
    print("🚀 البوت في وضع التوجيه الآن...")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()