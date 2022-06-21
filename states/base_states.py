from aiogram.dispatcher.filters.state import StatesGroup, State


class SupportMessageState(StatesGroup):
    '''Класс для машины состояний'''

    users_message = State()
