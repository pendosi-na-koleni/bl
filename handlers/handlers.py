from aiogram import Router, F
from aiogram.filters import StateFilter
from lexicon.phrases import texts
from aiogram.types import Message, CallbackQuery
from keyboards.handler_keyboards import cst_group_choice, english_lvl_choice, days
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.redis import RedisStorage, Redis
import table_scraper
from aiogram.types import FSInputFile
import json
from engl_scrap import dbe
import re
from aiogram.exceptions import TelegramBadRequest
redis = Redis(host='localhost')
storage = RedisStorage(redis=redis)
users = {}

def filter_cst_messages(message):
    pattern = r'^CST [1-9]$'
    if re.match(pattern, message):
        return True
    else:
        return False

class FSMGroupChoice(StatesGroup):
    cst_group = State()
    english_course = State()
    english_group = State()

handler_router = Router()
@handler_router.callback_query(F.data == "choice")
async def choice(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text=texts['choice'], reply_markup=cst_group_choice())
    await state.set_state(FSMGroupChoice.cst_group)


@handler_router.message(StateFilter(FSMGroupChoice.cst_group), lambda message: filter_cst_messages(message.text))
async def cst_choice(message: Message, state: FSMContext):
    await message.answer(text=texts['correct_choice_cst'], reply_markup=english_lvl_choice())
    await state.update_data(cst=message.text)
    await state.set_state(FSMGroupChoice.english_course)


@handler_router.callback_query(StateFilter(FSMGroupChoice.english_course))
async def english_course(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(text=texts['correct_choice_english'])
    await state.update_data(english_lvl=callback.data)
    await state.set_state(FSMGroupChoice.english_group)


@handler_router.message(StateFilter(FSMGroupChoice.cst_group), ~F.text.startswith("CST "))
async def incorrect_cst_choice(message: Message):
    p = FSInputFile("handlers/vatafak.jpg")
    await message.answer_photo(photo=p, caption=texts['incorrect_choice_cst'])


@handler_router.message(StateFilter(FSMGroupChoice.english_group), ~F.text.isdigit(), lambda x: int(x.text) not in range(1, 41))
async def incorrect_english_choice(message: Message):
    p = FSInputFile("handlers/vatafak.jpg")
    await message.answer_photo(photo=p, caption=texts["incorrect_choice_english"])


@handler_router.message(StateFilter(FSMGroupChoice.english_group), F.text.isdigit(), lambda x: int(x.text) in range(1, 41))
async def english_choice(message: Message, state: FSMContext):
    phh = FSInputFile("handlers/gud.jpg")
    await message.answer_photo(photo=phh, caption=texts["correct_group_choice"], reply_markup=days())
    await state.update_data(english_group=message.text)
    users[message.from_user.id] = await state.get_data()
    with open("database.json", 'w') as file:
        file.write(json.dumps(users))
    await state.clear()

@handler_router.message(lambda mess: mess.text in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
async def get_schedule(message: Message):
    with open("database.json", 'r') as file:
        f = json.load(file)
    if str(message.from_user.id) in list(f.keys()):
        try:
            await message.answer(text=table_scraper.get_group_schedule(f[str(message.from_user.id)]["cst"], message.text))
            for el in dbe:
                if el[0] == f[str(message.from_user.id)]["english_lvl"] and el[1]==f[str(message.from_user.id)]["english_group"] and el[2]==message.text:
                    await message.answer(text=f"{el[3]} Английский язык {el[4]}")
        except TelegramBadRequest:
            c = 0
            for el in dbe:
                if el[0] == f[str(message.from_user.id)]["english_lvl"] and el[1]==f[str(message.from_user.id)]["english_group"] and el[2]==message.text:
                    await message.answer(text=f"{el[3]} Английский язык {el[4]}")
                    c+=1
            if c == 0:
                await message.answer(text="You have no lessons at this day")

@handler_router.callback_query(F.data == "bulitin@hse.ru")
async def c1(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="bulitin@hse.ru")

@handler_router.callback_query(F.data == "memelyanova@hse.ru")
async def c2(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="memelyanova@hse.ru")

@handler_router.callback_query(F.data == "nbakulina@hse.ru")
async def c3(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="nbakulina@hse.ru")

@handler_router.callback_query(F.data == "ivkoldina@hse.ru")
async def c4(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="ivkoldina@hse.ru")

@handler_router.callback_query(F.data == "nvaseeva@hse.ru")
async def c5(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(text="nvaseeva@hse.ru")

