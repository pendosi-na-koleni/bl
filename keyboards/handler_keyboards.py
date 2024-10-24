from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardMarkup, ReplyKeyboardBuilder, InlineKeyboardMarkup, InlineKeyboardBuilder, InlineKeyboardButton

def cst_group_choice() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    buttons = [KeyboardButton(text=f"CST {i}") for i in range(1, 10)]
    kb_builder.row(*buttons, width=3)
    return kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

def english_lvl_choice() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    levels = ["Entry level", "Elementary", "Upper-Intermediate", "Advanced"]
    buttons = [InlineKeyboardButton(text=lvl, callback_data=lvl) for lvl in levels]
    builder.add(*buttons)
    return builder.as_markup()
def days() -> ReplyKeyboardMarkup:
    kb_builder = ReplyKeyboardBuilder()
    buttons = [KeyboardButton(text=f"{i}") for i in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']]
    kb_builder.row(*buttons, width=2)
    return kb_builder.as_markup(resize_keyboard=True)