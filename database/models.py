from datetime import datetime

from sqlalchemy import ForeignKey, VARCHAR, BigInteger
from sqlalchemy.orm import as_declarative, declarative_base, Mapped, mapped_column

# @as_declarative()
# class BaseModel:
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

BaseModel = declarative_base()


class UserModel(BaseModel):
    """
    Модель данных для представления пользователей в базе данных.

    :ivar user_id: Уникальный ID пользователя в Telegram.
    :ivar username: Username пользователя в Telegram.
    :ivar first_name: Имя пользователя в Telegram.
    :ivar last_name: Фамилия пользователя в Telegram.
    :ivar admin: Является ли пользователь администратором.
    :ivar registration_time: Время регистрации пользователя.
    """
    __tablename__ = "Users"

    user_id: Mapped[int] = mapped_column(BigInteger, nullable=False, primary_key=True, unique=True)
    username: Mapped[str] = mapped_column(VARCHAR(32), nullable=True)
    first_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    admin: Mapped[bool] = mapped_column(default=False)
    registration_time: Mapped[datetime] = mapped_column(default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"User: {self.username}, id: {self.user_id}"


class AddressModel(BaseModel):
    """
    Модель данных для представления адресов электронной почты пользователей в базе данных.

    :ivar id: ID адреса.
    :ivar user_id: Уникальный ID пользователя в Telegram.
    :ivar email: Адрес электронной почты пользователя.
    """
    __tablename__ = "Addresses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.user_id"))
    email: Mapped[str] = mapped_column()

    def __repr__(self):
        return f"E-mail: {self.email}"
