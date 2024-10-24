from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    button = InlineKeyboardButton(text="Select a group", callback_data="choice")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    return keyboard

def links():
    b1 = InlineKeyboardButton(text="VK cst group", url="https://vk.me/join/bnxRCF56_VbfnRi0zM990_kblWXH65w43e8=")
    b2 = InlineKeyboardButton(text="All textbooks", url="https://drive.google.com/drive/folders/1jsB6MoU5sor7DJvK6Cu8vgcCm3fZbroI?usp=sharing")
    b3 = InlineKeyboardButton(text="Guide from other courses students", url="https://vk.com/hsefirstyearguide")
    b4 = InlineKeyboardButton(text="Psychological assistance", url="http://cpc.pushpullme.ru/pub/form/add/lead.html")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[b1],[b2],[b3],[b4]])
    return keyboard

def curators():
    b1 = InlineKeyboardButton(text="CST1 Curator: Варвара Сливницина", url="https://t.me/varuushik")
    b2 = InlineKeyboardButton(text="CST2 Curator: Софья Субботина", url="https://t.me/mingilover3000")
    b3 = InlineKeyboardButton(text="CST3 Curator: Дарья Смирнова", url="https://t.me/Ddasmii")
    b4 = InlineKeyboardButton(text="CST4 Curator: 💪Кирилл Голотвин💪", url="https://t.me/sad_ukey")
    b5 = InlineKeyboardButton(text="CST5 Curator: Яна Захарченко", url="https://t.me/Yazzzna")
    b6 = InlineKeyboardButton(text="CST6 Curator: Ника Новожилова", url="https://t.me/nika_novoo")
    b7 = InlineKeyboardButton(text="CST7 Curator: Вадим Береснев", url="https://t.me/vadyukkha")
    b8 = InlineKeyboardButton(text="CST8 Curator: Егор Батяев", url="https://t.me/egorbatyaev")
    b9 = InlineKeyboardButton(text="CST9 Curator: Илья Шалявин", url="https://t.me/shalyavin")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[b1], [b2], [b3], [b4], [b5], [b6], [b7], [b8], [b9]])
    return keyboard

def contacts():
    b4 = InlineKeyboardButton(text="Начальник отдела сопровождения учебного процесса: Емельянова Мария Максимовна", callback_data="memelyanova@hse.ru")
    b2 = InlineKeyboardButton(text="Заместитель начальника: Полонецкая Наталья Александровна", callback_data="nbakulina@hse.ru")
    b3 = InlineKeyboardButton(text="Заместитель начальника: Колдина Лилия Валерьевна ", callback_data="ivkoldina@hse.ru")
    b1 = InlineKeyboardButton(text="Академический руководитель: 🏆Борис Игоревич Улитин🏆", callback_data="bulitin@hse.ru")
    b5 = InlineKeyboardButton(text=" Декан факультета ИМиКН: Асеева Наталья Владимировна", callback_data="nvaseeva@hse.ru")
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[b1], [b2], [b3], [b4], [b5]])
    return keyboard
