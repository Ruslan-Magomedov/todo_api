from fastapi import APIRouter

from src.config import settings


router = APIRouter(prefix="/todo", tags=["TODO"])


@router.get("/", summary="get db url")
def db_url():
    """ Функция возвращает ссылку для подключения к базе данных """
    return {"url": settings.db_url}
