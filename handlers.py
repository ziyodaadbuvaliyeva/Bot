from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    buttons = [
        ["Frontend darslari", "Backend darslari", "No Code darslari"],
        ["Dizaynerlik darslari", "Date Base", "Android"],
        ["Mobilografiya darslari"],
        ["SMM darslari", "Photoshop darslari"],
        ["Kiber xavfsizlik", "Videomontaj darslari"],
        ["Telegram Bot yaratish", "IOS"]
    ]
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    message = (
        "📌 Botni ishga tushirish uchun /start tugmasini bosing.\n\n"
        "👩‍💻 Admin: @Ziyoda\n"
        "👨‍💻 Dasturchi: @Ziyoda\n"
        "📢 Kanal: @ziyodaabduvaliyeva1bot\n\n"
        "Quyidagi kurslardan birini tanlang 👇"
    )
    update.message.reply_text(message, reply_markup=keyboard)



def make_menu(buttons, text, update):
    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    update.message.reply_text(text, reply_markup=keyboard)



def frontend_menu(update: Update, context: CallbackContext):
    buttons = [
        ["HTML darslari", "CSS darslari"],
        ["JavaScript darslari", "React darslari"],
        ["JDS darslari", "Bootstrap darslari"],
        ["TypeScript darslari"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Frontend bo'limi — quyidagilardan birini tanlang ", update)


def backend_menu(update: Update, context: CallbackContext):
    buttons = [
        ["C++ darslari", "Python darslari (Botir Ziyatov)"],
        ["Python darslari (Anvar Nazrullayev)"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, "🖥 Backend bo'limi — darslardan birini tanlang", update)


def nocode_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Telegram bot yaratish darslari", "Sayt yaratish darslari"],
        ["Kodsiz suniy intellekt yasash darsi"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " No Code bo'limi — darslardan birini tanlang", update)


def dizaynerlik_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Figma darslari", "Canva darslari"],
        ["Grafik dizayn darslari (Najot ta'lim)"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Dizaynerlik bo'limi — darslardan birini tanlang", update)


def database_menu(update: Update, context: CallbackContext):
    buttons = [
        ["PostgreSQL darslari", "MySQL darslari"],
        ["MongoDB darslari"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, "🗄 Data Base bo'limi — darslardan birini tanlang", update)


def android_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Kotlin darslari", "Java darslari"],
        ["Android darslari"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, "📱 Android bo'limi — darslardan birini tanlang", update)


def mobilografiya_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Milliy ta'lim resurslari", "Ustoz AI"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Mobilografiya bo'limi — darslardan birini tanlang", update)


def smm_menu(update: Update, context: CallbackContext):
    buttons = [
        ["AB.Studio", "Milliy ta'lim resurslari (SMM)"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " SMM bo‘limi — darslardan birini tanlang", update)


def photoshop_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Amu Web School", "IQ Design"],
        ["Enter Max", "Baxodirjon Mullajonov"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Photoshop bo‘limi — darslardan birini tanlang", update)


def kiber_menu(update: Update, context: CallbackContext):
    buttons = [
        ["IT House darslari", "Saud Abdulvahed darslari"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Kiber xavfsizlik — keraklisini tanlang", update)


def videomontaj_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Ustoz AI darslari", "Akmal Abdullayev"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Videomontaj — kerakli darsni tanlang", update)


def telegrambot_menu(update: Update, context: CallbackContext):
    buttons = [
        ["Sariq Dev", "Maqsadli Kundalik"],
        ["No Code", "PHP orqali bot"],
        ["⬅ Go back"]
    ]
    make_menu(buttons, " Telegram bot yaratish — kerakli uslubni tanlang", update)



video_links = {
    "HTML darslari": "https://youtu.be/qz0aGYrrlhU\nhttps://youtu.be/UB1O30fR-EE",
    "CSS darslari": "https://youtu.be/1PnVor36_40\nhttps://youtu.be/yfoY53QXEnI",
    "JavaScript darslari": "https://youtu.be/W6NZfCO5SIk\nhttps://youtu.be/PkZNo7MFNFg",
    "React darslari": "https://youtu.be/bMknfKXIFA8\nhttps://youtu.be/hQAHSlTtcmY",
    "JDS darslari": "https://youtube.com/playlist?list=PLnBvgoOXZNCPWSp9sU2kdJCSVgrYQP9Qu",
    "Bootstrap darslari": "https://youtu.be/-qfEOE4vtxE\nhttps://youtu.be/4sosXZsdy-s",
    "TypeScript darslari": "https://youtu.be/d56mG7DezGs\nhttps://youtu.be/zQnBQ4tB3ZA",
    "C++ darslari": "https://youtu.be/vLnPwxZdW4Y\nhttps://youtu.be/mUQZ1qmKlLY",
    "Python darslari (Botir Ziyatov)": "https://www.youtube.com/playlist?list=PLcQ79v2D6r7v9uUdd2FTMI1rGfCFN6D8x",
    "Python darslari (Anvar Nazrullayev)": "https://www.youtube.com/playlist?list=PLtX8LfA9DL7s7_J-0TTPeTU7lcVqKchxz",
    "Telegram bot yaratish darslari": "https://www.youtube.com/watch?v=2qpqPLF3GsA&list=PLynGQyFazHz_KbXnxJ8oA2CxyD7QOa5yJ",
    "Sayt yaratish darslari": "https://www.youtube.com/watch?v=8Ulu2iIbsuc&list=PLynGQyFazHz_TPrM9Ptq0MweY9L5OSOUJ",
    "Kodsiz suniy intellekt yasash darsi": "https://www.youtube.com/watch?v=VWqNfdX15HA",
    "Figma darslari": "https://www.youtube.com/playlist?list=PLUcsbZa0qzu3yN4qvJp3v3IpCZLf6U9YK",
    "Canva darslari": "https://www.youtube.com/watch?v=IO2h-1Ku-TI",
    "Grafik dizayn darslari (Najot ta'lim)": "https://www.youtube.com/playlist?list=PL3oGRRS1KdyMT27Np7lSEcQiA3fXq1LBP",
    "PostgreSQL darslari": "https://www.youtube.com/playlist?list=PL0lO_mIqDDFU4RmU-9dDz3M5jo6tSlsCQ",
}



def handle_message(update: Update, context: CallbackContext):
    text = update.message.text

    if text == "Frontend darslari":
        frontend_menu(update, context)
    elif text == "Backend darslari":
        backend_menu(update, context)
    elif text == "No Code darslari":
        nocode_menu(update, context)
    elif text == "Dizaynerlik darslari":
        dizaynerlik_menu(update, context)
    elif text == "Date Base":
        database_menu(update, context)
    elif text == "Android":
        android_menu(update, context)
    elif text == "Mobilografiya darslari":
        mobilografiya_menu(update, context)
    elif text == "SMM darslari":
        smm_menu(update, context)
    elif text == "Photoshop darslari":
        photoshop_menu(update, context)
    elif text == "Kiber xavfsizlik":
        kiber_menu(update, context)
    elif text == "Videomontaj darslari":
        videomontaj_menu(update, context)
    elif text == "Telegram Bot yaratish":
        telegrambot_menu(update, context)
    elif text == "IOS":
        update.message.reply_text("IOS bo'limi hozircha tayyor emas.")
    elif text in video_links:
        update.message.reply_text(video_links[text])
    elif text == "⬅ Go back":
        start(update, context)
    else:
        update.message.reply_text("Iltimos, menyudan tugmalar orqali tanlang yoki /start tugmasini bosing.")
