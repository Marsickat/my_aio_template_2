from aiogram.filters.callback_data import CallbackData


class NumbersCallbackFactory(CallbackData, prefix="numfab"):
    action: str
    value: int
