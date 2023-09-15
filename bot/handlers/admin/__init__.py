from os import getenv

from aiogram import Router

from .dice import router as dice_router
from bot.filters import IsAdminFilter

router = Router()
router.message.filter(IsAdminFilter(eval(getenv("ADMINS"))))
router.include_routers(dice_router)
