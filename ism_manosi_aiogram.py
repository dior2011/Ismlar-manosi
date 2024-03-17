import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from ism_manosi import ismlar_manosi


TOKEN = "6232855682:AAG-6BbtpsJND2WkXXGjG-UjgHNNvgU4WfY"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(text="Assalomu alaykum, ism yozing!")

@dp.message(F.text) 
async def ism_func(message: Message):
    text = ismlar_manosi(message.text)
    await message.answer(text=text)



async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())