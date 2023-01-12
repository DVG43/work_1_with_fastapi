from fastapi import FastAPI, Query
from shimas import Book
from typing import List

app = FastAPI()


# @app.get('/')
# def home():
#     return {"key": "hello"}
#
#
# @app.get('/{pk}')
# def get_item(pk: int, q: int = None):
#     return {"key": pk, "q": q}
#
#
# @app.get('/user/{pk}/item/{item}/')
# def get_user_item(pk: int, item: str):
#     return {"user": pk, "item": item}

@app.post('/book')
def create_book(item: Book):
    return item


#валидация по длинне строки
# @app.get('/book')
# def get_book(q: str = Query(None, min_length=3, max_length=8)):
#     return q


#добавка описание данных
# @app.get('/book')
# def get_book(q: str = Query(...,  description="search book")):  # три точки это обязательное значение,
#     return q


#ввод данных в виде списка
@app.get('/book')
def get_book(q: List[str] = Query("test",  description="search book", deprecated=True)):
    # если вмето точек поставить "test" то это дефолное значение
    # если вместо "test" ,   ["test1", "test 2]
    # это дефолтный список, deprecated=Tru это значит что 'test' устаревшее и будет удалено
    return q

