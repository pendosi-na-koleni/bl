from aiogram.types import BotCommand
from aiogram import Bot

async def set_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command="/start", description="enter or change groups"),
        BotCommand(command="/showdata", description="see your groups"),
        BotCommand(command="/links", description="useful links"),
        BotCommand(command="/curators", description="curator's contacts"),
        BotCommand(command="/contacts", description="important contacts"),
    ]

    await bot.set_my_commands(main_menu_commands)