from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from ai_chat import gerar_resposta
from config import TELEGRAM_BOT_TOKEN

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = update.message.text
    resposta = gerar_resposta(pergunta)
    await update.message.reply_text(resposta)

app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))

print("Bot rodando...")
app.run_polling()
