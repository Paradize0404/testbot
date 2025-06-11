from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states import NameSG


async def start_handler(message: Message, dialog_manager: DialogManager):
    """Обработчик команды /start"""
    await dialog_manager.start(NameSG.asking_name, mode=StartMode.RESET_STACK)


def register_handlers(dp: Dispatcher):
    """Регистрация всех обработчиков"""
    dp.message.register(start_handler, CommandStart())