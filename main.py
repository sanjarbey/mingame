from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "6425738546:AAHrll7HoQoh0BR3RhzLcVys1aHBnu5elrU"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    await message.answer("Mine Game o‘yinini boshlash uchun pastdagi tugmani bosing!", 
                         reply_markup=types.InlineKeyboardMarkup().add(
                             types.InlineKeyboardButton("O‘ynash", url="https://your-game-host.com/index.html")
                         ))

if __name__ == "__main__":
    executor.start_polling(dp)
