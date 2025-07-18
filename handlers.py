from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    buttons = [
        ["fronted darslari", "backend darslari", "No Code darslari"],
        ["dizaynerlik darslari", "Date Base", "Android"],
        ["Mobilografiya darslari"],
        ["SMM darslari", "Photoshop darslari"],
        ["Kiber xavfsizlik", "videomontaj darslari"],
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

    