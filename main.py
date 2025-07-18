from telegram.ext import Updater, CommandHandler
from config import BOT_TOKEN
from handlers import start

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
