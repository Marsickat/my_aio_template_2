from aiogram import types
from aiogram.filters import BaseFilter


class IsEmailFilter(BaseFilter):
    async def __call__(self, message: types.Message) -> bool:
        """
        Проверяет, содержит ли сообщение e-mail.

        Args:
            message (types.Message): Объект сообщения.

        Returns:
            bool: True, если сообщение содержит e-mail, иначе False.
        """
        entities = message.entities or []
        for item in entities:
            if item.type == "email":
                return True
        return False
