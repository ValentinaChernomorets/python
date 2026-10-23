from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
# step 2
from aiogram.filters import Command
import asyncio
 # 8900864391:AAF-BBlCITCK2uZLBgYcqgfJJLKL3BJfKTk
bot = Bot(
    token ='ВАШ TOKEN BOT FATHER',
    # token = '8649052999:AAFul7A7bPZ3I83GSjd3h0HH601OHO4aM2M',
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
# step 2
# @dp.message(Command("start"))
# async def echo(message: Message):
#     await message.answer("Hi friend!")
# Step 3
@dp.message(Command("start"))
async def echo(message: Message):
    name = input("What is your name?")
    await message.answer("Hi! " + name)

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
