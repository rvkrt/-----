from fastapi import FastAPI
import logging
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from playground.router import router as playground_router
from playground.exceptions import general_exception_handler

# Настройки приложения
app = FastAPI(
    title="Игровая площадка Нерф-арена",
    description="Веб сайт игровой площадки Нерф-арена",

    # Адрес для документации - если запускаешь
    # сайт для людей, то закоментируй!
    openapi_url="",
)

# подключаем обработчики путей к страницам
app.include_router(playground_router)

# Подключение папки static для обслуживания статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


origins = [
    "http://localhost:3000",
]

# Мидлвэйр
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Регистрация обработчиков исключений
app.add_exception_handler(Exception, general_exception_handler)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)