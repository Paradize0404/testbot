from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.text import Const, Format, Case
from aiogram_dialog.widgets.input import TextInput

from states import NameSG


async def name_handler(message: Message, widget, dialog_manager: DialogManager, name: str):
    """Обработчик ввода имени пользователя"""
    # Сохраняем имя в данные диалога
    dialog_manager.dialog_data["user_name"] = name
    dialog_manager.dialog_data["greeting_shown"] = True


async def get_data(dialog_manager: DialogManager, **kwargs):
    """Геттер данных для диалога"""
    return {
        "user_name": dialog_manager.dialog_data.get("user_name", ""),
        "greeting_shown": dialog_manager.dialog_data.get("greeting_shown", False)
    }


# Создаем диалог с одним окном
name_dialog = Dialog(
    Window(
        Case(
            {
                True: Format("Привет, {user_name}!"),
                False: Const("Как тебя зовут?"),
            },
            selector="greeting_shown"
        ),
        TextInput(
            id="name_input",
            type_factory=str,
            on_success=name_handler,
            when="~greeting_shown"  # Показываем поле ввода только когда приветствие не показано
        ),
        state=NameSG.asking_name,
        getter=get_data,
    ),
)