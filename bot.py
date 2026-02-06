import os
from flask import Flask, request
import telegram

TOKEN = os.environ.get(8595233518:AAHYLmSC7LJmK3WmX53iORCN4JinOzU1vOs)
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    if update.message and update.message.text == "/start":
        bot.send_message(
            chat_id=update.message.chat_id,
            text="Yes! I am alive "
        )
    return "ok"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))