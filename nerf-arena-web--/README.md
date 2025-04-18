# Документация для проекта "Игровая площадка Нерф-арена"

![image](https://github.com/user-attachments/assets/5e8d8b54-f66d-4441-821e-d7e4aafe315e)



## Описание
Проект представляет собой веб-сайт для игровой площадки "Нерф-арена". Сайт включает в себя страницы с информацией о проекте, контактные данные и функциональные элементы, такие как кнопки и всплывающие окна.

Приложение разработано на основе FastAPI и включает маршруты для предоставления страниц, обработку исключений, а также мидлвэйры для работы с CORS и обслуживания статических файлов.

## Реализованные функции
- **Главная страница**: Отображает заголовок, описание проекта и логотип.
- **Контакты**: Отдельная страница с контактной информацией.
- **Всплывающее окно**: Всплывающее окно с контактными данными, активируемое кнопкой.
- **Статические файлы**: Использование Bootstrap CSS для стилизации интерфейса.

## Структура проекта
- **`web/playground/router.py`**: Файл с определением маршрутов для веб-страниц.
- **`web/playground/exceptions.py`**: Файл с кастомными исключениями и обработчиками ошибок.
- **`web/static`**: Директория для хранения статических файлов, таких как CSS и изображения.
- **`web/main.py`**: Основной файл для запуска FastAPI приложения.

## Используемые технологии
- **`FastAPI`**: Современный фреймворк для разработки веб-приложений на Python.
- **`Jinja2`**`: Шаблонизатор для создания HTML-страниц.
- **`Starlette`**: Легковесный ASGI фреймворк, на основе которого построен FastAPI.
- **`Bootstrap`**: CSS-фреймворк для создания адаптивного и современного интерфейса.

## Локальный запуск
- **`uvicorn web.main:app--reload`**
