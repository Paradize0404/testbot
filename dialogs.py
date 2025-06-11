from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import TextInput

from states import NameSG


async def name_handler(message: Message, widget, dialog_manager: DialogManager, name: str):
    """Обработчик ввода имени пользователя"""
     # Сохраняем имя и переключаем окно на приветствие
    dialog_manager.dialog_data["user_name"] = name
    await dialog_manager.switch_to(NameSG.greeted)


async def get_data(dialog_manager: DialogManager, **kwargs):
    """Геттер данных для диалога"""
    return {
        "user_name": dialog_manager.dialog_data.get("user_name", "")
    }


# Создаем диалог с двумя окнами
name_dialog = Dialog(
    Window(
        Const("Как тебя зовут?"),
        TextInput(
            id="name_input",
            type_factory=str,
            on_success=name_handler,
        ),
        state=NameSG.asking_name,
        getter=get_data,
    ),
        Window(
        Format("Привет, {user_name}!"),
        state=NameSG.greeted,
        getter=get_data,
    ),
)