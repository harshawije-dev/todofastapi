from fastapi import FastAPI
from fastapi.params import Body
from typing import Union
from src.security.validation.todo import Todo

app = FastAPI()


# Defining index route


@app.get('/')
def _root():
    return {
        "message": "Success",
        "response": "Hello World"
    }


@app.get('/todos/{product_id}')
async def _get_products(product_id: int, q: Union[str, None] = None):
    return {
        "message": "Success",
        "id": product_id,
        "q": q
    }


@app.post('/todo/create')
async def _create_todo(payload: dict = Body(...)):
    return {
        "message": "Success",
        "data": payload
    }
