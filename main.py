from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import Message, CallbackQuery
from keyb import keyb, create_menu, create_question
from aiogram import F
from translations import texts
import logging
# Step 8
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)

logging.info("Bot started")

# step 2
from aiogram.filters import Command
import asyncio
bot = Bot(
    # token ='ВАШ TOKEN BOT FATHER',
    token = '9245889231:AAH6gJBtFrWqGZEaI0ABU6RXjEnVej3W3CA',
    default = DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())

# @dp.message()
# async def echo(message: Message):
#     await message.answer(message.text)
# ---------------------------------------------------------//------------------------------//---------------------------------
# step 2
# @dp.message(Command("start"))
# async def echo(message: Message):
#     await message.answer("Hi friend!")

# ---------------------------------------------------------//------------------------------//---------------------------------
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

# ---------------------------------------------------------//------------------------------//---------------------------------
# # Step 4
# @dp.message(Command("start"))
# async def echo(message: Message):
#     await message.answer(
#         "Hello! 🖐️ Welcome to School Marina Velixar!🏫\n"
#         "What language to speak do you prefer?\n"
#         "Enter: RU, MD или EN", reply_markup=keyb)
    
# @dp.message(F.text == "🇷🇺 RU")
# async def russian(message: Message):
#     await message.answer("Здравствуйте! Вас приветствует школа School Marina Velixar! Чем можем Вам помочь?")
# @dp.message(F.text == "🇲🇩 MD")
# async def moldovan(message: Message):
#     await message.answer("Bună ziua! Școala Marina Velixar vă urează bun venit! Cum te putem ajuta?")
# @dp.message(F.text == "🇬🇧 EN")
# async def english(message: Message):
#     await message.answer("Hello! Welcome to School Marina Velixar! How we can help you?")

# ---------------------------------------------------------//------------------------------//---------------------------------
# Step 5 Home Work.
# @dp.message(Command("start"))
# async def echo(message: Message):
#     await message.answer(
#         "Hello! 🖐️ Welcome to School Marina Velixar!🏫\n"
#         "What language to speak do you prefer?\n"
#         "Enter: RU, MD или EN", reply_markup=keyb)
# @dp.message(F.text == "🇷🇺 RU")
# async def russian(message: Message):
#     await message.answer("Здравствуйте! Вас приветствует школа School Marina Velixar! Чем можем Вам помочь?", reply_markup=keyb_menu)
# @dp.message(F.text == "🇲🇩 MD")
# async def moldovan(message: Message):
#     await message.answer("Bună ziua! Școala Marina Velixar vă urează bun venit! Cum te putem ajuta?", reply_markup=keyb_menu)
# @dp.message(F.text == "🇬🇧 EN")
# async def english(message: Message):
#     await message.answer("Hello! Welcome to School Marina Velixar! How we can help you?", reply_markup=keyb_menu)

# @dp.message(F.text == "contacts")
# async def english(message: Message):
#     await message.answer(
#         "Name: Marina Velixar School\n"
#         "Адрес: Strada Alexei Şciusev 98a \n"
#         "phone: +373(78).......\n"
#         "Email: marinavelixar@gmail.com\n"
#         '<a href="https://www.instagram.com/school_marinavelixar/">Instagram</a>')

# ---------------------------------------------------------//------------------------------//---------------------------------
# Step 6 Create buttons depending on language
# Create variable to save user language - user_languages
user_languages = {}
@dp.message(Command("start"))
async def echo(message: Message):
    await message.answer(
        "Hello! 🖐️ Welcome to School Marina Velixar!🏫\n"
        "What language to speak do you prefer?\n"
        "Enter: RU, MD или EN", reply_markup=keyb)
# RUSSIAN
@dp.message(F.text == "🇷🇺 RU")
async def russian(message: Message):
    user_languages[message.from_user.id] = "ru"
    await message.answer(
        texts["ru"]["welcome"],
        reply_markup=create_menu("ru")
    )
# ROMANIAN
@dp.message(F.text == "🇲🇩 MD")
async def moldovan(message: Message):
    user_languages[message.from_user.id] = "ro"
    await message.answer(
        texts["ro"]["welcome"],
        reply_markup=create_menu("ro")
    )
# ENGLISH
@dp.message(F.text == "🇬🇧 EN")
async def english(message: Message):
    user_languages[message.from_user.id] = "en"
    await message.answer(
        texts["en"]["welcome"],
        reply_markup=create_menu("en")
    )

# CONTACTS
@dp.message(F.text.in_([
    "Контакты",
    "Contacte",
    "Contacts"
]))
async def show_contacts(message: Message):
    language = user_languages.get(message.from_user.id, "ru")
    await message.answer(
        texts[language]["contacts"]
    )
# Step 7
# Inline question
@dp.message(Command("question"))
async def start(message: Message):
    language = user_languages.get(message.from_user.id, "ru")
    
    # debug
    print("USER ID:", message.from_user.id)
    print("LANGUAGE:", language)
    print("TEXT:", texts[language]["question_contact"]["welcome"])

    await message.answer(
        texts[language]["question_contact"]["welcome"],
        reply_markup=create_question(language)
    )

@dp.callback_query(F.data == "add_channel")
async def add_channel(callback: CallbackQuery):
    language = user_languages.get(callback.from_user.id, "ru")
    await callback.answer()
    await callback.message.answer(
        texts[language]["question_contact"]["add_channel"]
    )

@dp.callback_query(F.data == "no_channel")
async def no_channel(callback: CallbackQuery):
    language = user_languages.get(callback.from_user.id, "ru")
    await callback.answer()
    await callback.message.answer(
        texts[language]["question_contact"]["no_channel"]
    )

# Step 8
class Registration(StatesGroup):
    name = State()
    age = State()
    date = State()

@dp.message(Command("registration"))
async def from_FSM(message:Message, state: FSMContext):
    # Task add lounguage param. And create multilanguage.
    # language = user_languages.get(message.from_user.id, "ru")
    # print(language)
    await message.answer("Hi, enter your name, please.")
    await state.set_state(Registration.name)

@dp.message(Registration.name)
async def name_FSM(message:Message, state: FSMContext):
    await message.answer("Thank you! Now enter your age.")
    await state.update_data(name=message.text)
    await state.set_state(Registration.age)

@dp.message(Registration.age)
async def name_FSM(message:Message, state: FSMContext):
    await message.answer("Thank you! Enter please the date when you want to start.")
    await state.update_data(age=message.text)
    await state.set_state(Registration.date)

@dp.message(Registration.date)
async def name_FSM(message:Message, state: FSMContext):
    await state.update_data(date=message.text)
    data = await state.get_data()
    print(data)
    await message.answer("Thank you! Your request sent.")
    await state.clear()

# Examples for Class
# class Car:
#     def __init__(self, color, brand):
#         self.color = color
#         self.brand = brand

#     def drive(self):
#         print("Автомобиль едет!")

# car1 = Car("Красный", "BMW")
# car2 = Car("Синий", "Audi")
# Examples for Class

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())
