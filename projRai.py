import os
from flask import Flask
from telegram.ext import Application, CommandHandler
from telegram import Update

app = Flask(__name__)
BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"

# تعريف دالة البداية
async def start(update: Update, context):
    await update.message.reply_text("البوت يعمل بنجاح!")

# إعداد التطبيق
application = Application.builder().token(BOT_TOKEN).build()
application.add_handler(CommandHandler("start", start))

@app.route('/')
def home():
    return "البوت يعمل"

# تشغيل البوت في الخلفية عند بدء تطبيق Flask
if __name__ == "__main__":
    # هذا التشغيل مخصص للبيئات التي تدعم Polling
    # إذا استمرت مشكلة Render، سنحتاج لتغيير الاستراتيجية إلى Background Thread
    import threading
    
    def run_bot():
        application.run_polling()

    threading.Thread(target=run_bot, daemon=True).start()
    
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)