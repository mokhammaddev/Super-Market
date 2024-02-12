from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Boshlash"),
        # BotCommand(command="help", description="Yordam"),
        # BotCommand(command="cancel", description="O'chirish"),
        # BotCommand(command="inline", description="Inline tugmalarini ko'rsatish")
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
