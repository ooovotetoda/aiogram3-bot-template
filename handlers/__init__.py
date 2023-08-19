from aiogram import Router


def setup_routers() -> Router:
    from . import start, error_handler, echo

    router = Router()
    router.include_router(start.router)
    router.include_router(echo.router)
    router.include_router(error_handler.router)
    
    return router
