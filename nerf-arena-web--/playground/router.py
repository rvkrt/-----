from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Фронтенд - шаблоны
templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix = "/main",
    tags=["Игровая площадка",
          "Нерф-арена",
          "Десткая игровая площадка"
          ]
)

@router.get("/")
async def read_root(request: Request):
    """
    Домашняя страница сайта
    :param request: запрос фастапи
    :return: шаблон Jinja
    """
    return templates.TemplateResponse("index.html", {
        "request": request,
        "title": "БИТВА НЕРФ",
        "description": "Захватывающие командные игры с бластерами Nerf!"
                       " Подходит для детей от 6 лет."
                       " Присоединяйтесь к нам для веселого и активного"
                       " времяпровождения :)"
    })

@router.get("/")
async def read_project(request: Request):
    """
    Страница с контактами
    :param request: запрос фастапи
    :return: шаблон Jinja
    """
    return templates.TemplateReяsponse("project.html", {"request": request})

