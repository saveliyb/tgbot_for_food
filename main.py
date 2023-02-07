import aiogram
from aiogram import types
import config
import logging
from keyboards import choosing_meal_kb, delete_kb
from parsing import Parser
from parsing_pdf import ParserPDF
from bot_dialog import Dialogs

logging.basicConfig(level=logging.INFO)

bot = aiogram.Bot(token=config.TOKEN)
dp = aiogram.Dispatcher(bot)

parser = Parser()
parser_pdf = ParserPDF()


@dp.message_handler(commands=['q', "start"])
async def process_start_command(message: types.Message):
    await message.reply(Dialogs.greeting, reply_markup=choosing_meal_kb)


@dp.message_handler(commands=['h', "help"])
async def process_start_command(message: types.Message):
    await message.reply(Dialogs.support, reply_markup=choosing_meal_kb)


def answer_message(message: str):
    if message[1:-1].lower() in ["завтрак", "обед", "ужин"]:
        return Dialogs.get_food_list(parser.get_menu(message[1:-1].lower()), message[1:-1])
    return "Оу, извини, я не понял что ты сказал"


@dp.message_handler(commands=["a"])
async def main_func(message: types.Message):
    """спарвка обычного юзера"""
    await message.reply("Убираем шаблоны сообщений", reply_markup=delete_kb)


@dp.message_handler(commands=["url"])
async def set_url(message: types.Message):
    if message.from_user.id == config.admin_id:
        parser.set_url(message.text.split()[1])
        # await parser.get_file()
        if await parser.get_file():
            parser_pdf.save_in_txt()
            await message.reply("новое расписание загружено")
        else:
            await message.reply("возникла непредвиденная ошибка")


@dp.message_handler()
async def main_func(message: types.Message):
    """спарвка обычного юзера"""
    await message.answer(answer_message(message.text))


if __name__ == '__main__':
    aiogram.executor.start_polling(dp)