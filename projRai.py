# كود مقترح لأوامر start و help
def start(update, context):
    message = """**تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.

للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل: @GCSBook_bot

نعتذر عن أي إزعاج، وشكراً لتفهمكم."""
    update.message.reply_text(message, parse_mode='Markdown')

def help_command(update, context):
    message = """**تنبيه هام:** تم إيقاف خدمة الاستعلام عبر هذا البوت لأغراض الصيانة والتحديث.

للاستمرار في الاستعلام عن بياناتك ومستحقاتك، يرجى الانتقال فوراً للبوت البديل: @GCSBook_bot

نعتذر عن أي إزعاج، وشكراً لتفهمكم."""
    update.message.reply_text(message, parse_mode='Markdown')