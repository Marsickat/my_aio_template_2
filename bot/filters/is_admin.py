from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdminFilter(BaseFilter):
    def __init__(self, admins: list):
        self.admins = admins

    async def __call__(self, message: Message) -> bool:
        """
        Проверяет, есть ли ID пользователя в списке администраторов.

        Args:
            message (Message): Объект сообщения.

        Returns:
            bool: True, если ID пользователя находится в списке администраторов, иначе False.
        """
        return message.from_user.id in self.admins
