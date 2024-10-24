import json
from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from keyboards.command_keyboards import start_keyboard, links, curators, contacts
from lexicon.phrases import commands
from aiogram.types import FSInputFile


command_router = Router()
@command_router.message(CommandStart())
async def start_message(message: Message):
    ph = FSInputFile("handlers/helo.jpg")
    await message.answer_photo(photo=ph, caption=commands['start'], reply_markup=start_keyboard())

@command_router.message(Command(commands=['showdata']))
async def show_data(message: Message):
    with open("database.json", 'r') as f:
        data = json.load(f)
    data = data[str(message.from_user.id)]
    await message.answer(text=f"CST group: {data['cst']}\n"
                              f"English level: {data['english_lvl']}\n"
                              f"English group: {data['english_group']}")

@command_router.message(Command(commands=['links']))
async def show_links(message: Message):
    p = FSInputFile("handlers/na_svyazi.jpg")
    await message.answer_photo(photo=p, caption="Check it!", reply_markup=links())

@command_router.message(Command(commands=['curators']))
async def show_links(message: Message):
    p = FSInputFile("handlers/curss.jpg")
    await message.answer_photo(photo=p, caption="Elite of the Elite", reply_markup=curators())

@command_router.message(Command(commands=['contacts']))
async def show_links(message: Message):
    p = FSInputFile("handlers/alye.jpg")
    await message.answer_photo(photo=p, caption="Troubles? Better call them!", reply_markup=contacts())