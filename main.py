from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message
from keyb import keyb
from aiogram import F

# step 2
from aiogram.filters import Command
import asyncio
bot = Bot(
    # token ='ВАШ TOKEN BOT FATHER',
    token = '9245889231:AAH6gJBtFrWqGZEaI0ABU6RXjEnVej3W3CA',
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
# @dp.message(Command("start"))
# async def echo(message: Message):
#     await message.answer(
#         "Hello! Welcome to School Marina Velixar!\n"
#         "What language to speak do you prefer?\n"
#         "Enter: RU, MD или EN")
        
# @dp.message()
# async def language(message: Message):
#     language = message.text.upper()
#     if language == "RU":
#         message_user = "Здравствуйте! Вас приветствует школа School Marina Velixar! Чем можем Вам помочь?"
#     elif language == "MD":
#         message_user = "Bună ziua! Școala Marina Velixar vă urează bun venit! Cum te putem ajuta?"
#     elif language == "EN":
#         message_user = "Hello! Welcome to School Marina Velixar! How we can help you?"
#     else:
#         message_user = "Пожалуйста, выберите RU, MD или EN."
#     await message.answer(message_user)

# Step 4
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer(
        "Hello! 🖐️ Welcome to School Marina Velixar!🏫\n"
        "What language to speak do you prefer?\n"
        "Enter: RU, MD или EN", reply_markup=keyb)
    
@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    await message.answer("Здравствуйте! Вас приветствует школа School Marina Velixar! Чем можем Вам помочь?")
@dp.message(F.text == "🇲🇩 MD")
async def moldovan(message: Message):
    await message.answer("Bună ziua! Școala Marina Velixar vă urează bun venit! Cum te putem ajuta?")
@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    await message.answer("Hello! Welcome to School Marina Velixar! How we can help you?")

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
