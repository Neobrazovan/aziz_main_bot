
from aiogram import Bot, Dispatcher, types, executor
import logging

API_TOKEN = "7985603336:AAHMGuEskuBYRWBC3KT1YAFdnPTRWLy5ifA"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Привет! Это основной бот.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
