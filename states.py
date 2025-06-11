from aiogram.fsm.state import State, StatesGroup


class NameSG(StatesGroup):
    """Группа состояний для диалога имени"""
    asking_name = State()
    greeted = State()