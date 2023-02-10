from src.floader_objs import telegram_floader
import json


def main(pic_data):
    pic_data = json.loads(pic_data)
    telegram_floader(pic_data)
