from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import BOT_TOKEN
from handlers import (
    start, handle_message,
    frontend_menu, backend_menu, nocode_menu,
    dizaynerlik_menu, database_menu, android_menu,
    mobilografiya_menu, smm_menu, photoshop_menu,
    kiber_menu, videomontaj_menu, telegrambot_menu
)

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('frontend', frontend_menu))
    dp.add_handler(CommandHandler('backend', backend_menu))
    dp.add_handler(CommandHandler('nocode', nocode_menu))
    dp.add_handler(CommandHandler('dizaynerlik', dizaynerlik_menu))
    dp.add_handler(CommandHandler('database', database_menu))
    dp.add_handler(CommandHandler('android', android_menu))
    dp.add_handler(CommandHandler('mobilografiya', mobilografiya_menu))
    dp.add_handler(CommandHandler('smm', smm_menu))
    dp.add_handler(CommandHandler('photoshop', photoshop_menu))
    dp.add_handler(CommandHandler('kiber', kiber_menu))
    dp.add_handler(CommandHandler('videomontaj', videomontaj_menu))
    dp.add_handler(CommandHandler('telegrambot', telegrambot_menu))


    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
