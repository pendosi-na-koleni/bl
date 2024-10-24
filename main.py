import asyncio
from aiogram import Bot, Dispatcher
from configuration.config import Config, load_config
from handlers.command_handlers import command_router
from handlers.handlers import handler_router
from main_menu.menu import set_menu


async def main():
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()
    dp.include_router(handler_router)
    dp.include_router(command_router)
    await set_menu(bot)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())