from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from ai_chat import gerar_resposta
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not TELEGRAM_TOKEN or not OPENROUTER_API_KEY:
    raise EnvironmentError("As variáveis TELEGRAM_TOKEN e OPENROUTER_API_KEY não estão definidas.")

async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = update.message.text
    print(f"[Pergunta recebida] {pergunta}")
    
    try:
        resposta = gerar_resposta(pergunta)
        await update.message.reply_text(resposta)
        print(f"[Resposta enviada] {resposta}")
    except Exception as e:
        print(f"[Erro] Falha ao gerar resposta: {e}")
        await update.message.reply_text("Desculpe, ocorreu um erro ao tentar responder.")

def main():
    print("Bot rodando...")

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == "__main__":
    main()
