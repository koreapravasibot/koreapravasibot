import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

@dp.message()
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Salom 👋")]],
        resize_keyboard=True
    )
    await message.answer("Bot ishlayapti ✅", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
