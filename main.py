from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

# هنجيب الـ TOKEN من متغير البيئة في Heroku
TOKEN = os.getenv("TOKEN")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً 👋 البوت بتاعك شغال على Heroku 🎉")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("الأوامر المتاحة:\n/start - بدء المحادثة\n/help - المساعدة")

def main():
    app = Application.builder().token(TOKEN).build()

    # أوامر البوت
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # التشغيل (Polling)
    app.run_polling()

if __name__ == "__main__":
    main()
