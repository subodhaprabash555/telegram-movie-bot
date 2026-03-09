from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8675108417:AAFIrkLl-fit8GGMXmjrOrfGkhaQHRwEXts"
CHANNEL_ID = "@moviestream_PS"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        msg_id = int(context.args[0])

        await context.bot.copy_message(
            chat_id=update.effective_chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=msg_id
        )
    else:
        await update.message.reply_text("Welcome to Movie Bot")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Running...")
app.run_polling()