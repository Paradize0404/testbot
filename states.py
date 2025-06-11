from aiogram.fsm.state import State, StatesGroup


class NameSG(StatesGroup):
    """Группа состояний для запроса имени"""
    asking_name = State()