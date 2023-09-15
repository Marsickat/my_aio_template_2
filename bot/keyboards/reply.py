from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def yes_no() -> ReplyKeyboardMarkup:
    """
    Генерирует текстовую клавиатуру с кнопками "Да" и "Нет".

    Returns:
         Текстовая клавиатура с кнопками "Да" и "Нет".
    """
    keyboard = [
        [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
    ]
    markup = ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите кнопку"
    )
    return markup
    # keyboard = ReplyKeyboardBuilder()
    # keyboard.button(text="Да")
    # keyboard.button(text="Нет")
    # keyboard.adjust(2)
    # return keyboard.as_markup(resize_keyboard=True, input_field_placeholder="Выберите кнопку")
