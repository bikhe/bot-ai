import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message 
from pymarkovchain import MarkovChain
from aiogram.types.bot_command import BotCommand
from aiogram import Router

ai = MarkovChain('./ai')

route = Router()

async def echo(message: Message):
    if message.text == "/gen":
        temp = ai.generateString()
        await message.answer(text=temp)
    else:
        ai.generateDatabase(message.text)
        ai.dumpdb()
    



async def start():
    bot = Bot(token='7193813052:AAH5aKJjtvxvSZGw0pWutXv030fHzPK6CDY')
    dp = Dispatcher()

    dp.message.register(echo)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())