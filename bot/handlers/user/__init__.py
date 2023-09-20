from aiogram import Router

from .echo import router as echo_router
from .addresses import router as addresses_router
from .inline_url import router as inline_url_router
from .nums_fab_cb import router as nums_fab_cb_router
from .aio_example_fsm import router as aio_example_fsm_router
from .starts import router as starts_router

router = Router()
router.include_routers(
    echo_router,
    addresses_router,
    inline_url_router,
    nums_fab_cb_router,
    aio_example_fsm_router,
    starts_router
)
