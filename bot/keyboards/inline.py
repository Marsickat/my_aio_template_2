from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callbacks import NumbersCallbackFactory


def inline_url_kb() -> InlineKeyboardBuilder:
    """
    Генерирует inline-клавиатуру с ссылкой на GitHub.

    Returns:
        Builder-объект inline-клавиатуры.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="Мой GitHub", url="https://github.com/Marsickat")
    return builder


def numbers_fab_kb() -> InlineKeyboardMarkup:
    """
    Генерирует inline-клавиатуру с действиями над числом.

    Returns:
         Inline-клавиатура с действиями над числом.
    """
    builder = InlineKeyboardBuilder()
    builder.button(text="-2", callback_data=NumbersCallbackFactory(action="change", value=-2))
    builder.button(text="-1", callback_data=NumbersCallbackFactory(action="change", value=-1))
    builder.button(text="1", callback_data=NumbersCallbackFactory(action="change", value=1))
    builder.button(text="2", callback_data=NumbersCallbackFactory(action="change", value=2))
    builder.button(text="Подтвердить", callback_data=NumbersCallbackFactory(action="finish", value=0))
    builder.adjust(4)
    return builder.as_markup()
