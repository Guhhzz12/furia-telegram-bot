FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80

ENV TELEGRAM_TOKEN=""
ENV OPENROUTER_API_KEY=""

CMD ["python3", "bot.py"]
