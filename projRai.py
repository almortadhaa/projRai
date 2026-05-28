import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask
from threading import Thread

# 1. إعداد السجلات (Logs) لمتابعة عمل البوت
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 2. إعداد Flask ليعمل البوت كخدمة ويب (لإرضاء Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "البوت يعمل الآن بنجاح!"

def run_flask():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

# 3. وظيفة أمر البداية /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="أهلاً بك! أنا البوت الجديد، كيف يمكنني مساعدتك اليوم؟"
    )

if __name__ == '__main__':
    # جلب التوكن من المتغيرات (Environment Variables)
    TOKEN = os.environ.get("BOT_TOKEN")
    
    # تشغيل Flask في خيط (Thread) منفصل
    Thread(target=run_flask).start()
    
    # تشغيل بوت تيليجرام
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("🚀 البوت بدأ العمل الآن...")
    application.run_polling()