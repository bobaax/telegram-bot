from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

TOKEN = os.getenv("8135596352:AAGRjnd_QlatLI6UdPhDhQFaxxEXQtoJ1po")

# ---------------- START ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📘 Year 1", callback_data="year1")],
        [InlineKeyboardButton("📗 Year 2", callback_data="year2")]
    ]
    await update.message.reply_text("اختر السنة:", reply_markup=InlineKeyboardMarkup(keyboard))

# ---------------- BUTTON HANDLER ----------------
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data
    parts = data.split("_")  # مثال: ["year1", "sem1", "lectures"]

    # ---------------- اختيار السنة ----------------
    if data.startswith("year") and len(parts) == 1:
        year = parts[0]
        keyboard = [
            [InlineKeyboardButton("Semester 1", callback_data=f"{year}_sem1")],
            [InlineKeyboardButton("Semester 2", callback_data=f"{year}_sem2")]
        ]
        await query.edit_message_text("اختر الترم:", reply_markup=InlineKeyboardMarkup(keyboard))

    # ---------------- اختيار الترم ----------------
    elif len(parts) == 2 and parts[1].startswith("sem"):
        year, sem = parts
        keyboard = [
            [InlineKeyboardButton("Lectures", callback_data=f"{year}_{sem}_lectures")],
            [InlineKeyboardButton("Sections", callback_data=f"{year}_{sem}_sections")],
            [InlineKeyboardButton("Links", callback_data=f"{year}_{sem}_links")]
        ]
        await query.edit_message_text("اختر نوع المحتوى:", reply_markup=InlineKeyboardMarkup(keyboard))

    # ---------------- اختيار المحتوى ----------------
    elif len(parts) == 3:
        year, sem, content = parts
        if content == "lectures":
            await query.edit_message_text(f"📚 Lectures for {year.upper()} - {sem.upper()}:\n- Lecture 1\n- Lecture 2")
        elif content == "sections":
            await query.edit_message_text(f"📝 Sections for {year.upper()} - {sem.upper()}:\n- Section 1\n- Section 2")
        elif content == "links":
            await query.edit_message_text(f"🔗 Links for {year.upper()} - {sem.upper()}:\n- Link 1\n- Link 2")

# ---------------- MAIN ----------------
def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()


