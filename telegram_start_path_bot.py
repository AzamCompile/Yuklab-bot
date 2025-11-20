from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from pathlib import Path
import sys

# Tokeningizni shu joyga qo‘ying
TELEGRAM_TOKEN = "8426511417:AAFvf03cJitDa-1fO4oeG6_fZVPYSWD8-4w"

def get_running_path() -> str:
    try:
        return str(Path(__file__).resolve())
    except NameError:
        exe = Path(sys.executable).resolve()
        if exe.name.lower().startswith("python"):
            return str(Path.cwd())
        return str(exe)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Start — Ko‘rsat", callback_data="show_path")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Bot ishga tushdi. Tugmani bosing:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "show_path":
        path = get_running_path()
        await query.edit_message_text(text=f"Bot fayl joylashuvi:\n`{path}`", parse_mode="MarkdownV2")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Noma'lum buyruq. /start yuboring.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.COMMAND, unknown))

    print("Bot ishga tushmoqda...")
    app.run_polling()

if __name__ == "__main__":
    main()
