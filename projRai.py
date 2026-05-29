import os
import threading
from flask import Flask, request
from telegram.ext import Application, CommandHandler
from telegram import Update

BOT_TOKEN = "8404596881:AAEbLEav6Vj6dG_UzIrMfGMOBX9PZfwuSt0"
app = Flask(__name__)

# إعداد البوت
bot_app = Application.builder().token(BOT_TOKEN).build()

async def start(update, context):
    await update.message.reply_text("البوت يعمل الآن بنظام Webhook ومسار منفصل!")

bot_app.add_handler(CommandHandler("start", start))

# دالة معالجة التحديثات (تعمل بشكل متزامن داخل Flask)
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data:
        # إرسال التحديث إلى queue البوت ليتم معالجته داخلياً
        bot_app.update_queue.put(Update.de_json(json_data, bot_app.bot))
        return "OK", 200
    return "Invalid", 400

@app.route('/')
def home():
    return "البوت جاهز."

# تشغيل البوت في الخلفية (Thread)
def run_bot():
    bot_app.run_polling() # هذا سيعمل في الخلفية بعيداً عن Flask

if __name__ == "__main__":
    # تشغيل البوت في مسار منفصل
    threading.Thread(target=run_bot, daemon=True).start()
    # تشغيل خادم الويب
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))