import telebot
import os
from base64 import b64decode

def telegram_floader(file_data):
    """
    Посылает фото в чат Телеграмм.
    :return:
    """
    # Пока только 1 бот и 1 чат, в будущем придётся пилить мапперы
    bot = telebot.TeleBot(os.environ.get('telegram_bot_1'))
    fdata = b64decode(file_data.get('fdata'))
    bot.send_photo(file_data.get('chat_id'), fdata)
