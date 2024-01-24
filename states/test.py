from aiogram.filters.state import StatesGroup, State


class RandomState(StatesGroup):
    name_amount = State()
    name = State()


class AdminState(StatesGroup):
    are_you_sure = State()
    ask_ad_content = State()