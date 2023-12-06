from typing import Union
from redis_om import get_redis_connection, HashModel
from fastapi import FastAPI
import os
from config import settings


app = FastAPI()

redis = get_redis_connection(
    host=settings.host,
    port=settings.port,
    password=settings.password,
    decode_responses=True,
)


class Product(HashModel):
    name: str
    price: float
    quantity: int

    class Meta:
        database = redis


def format(pk: str):
    product = Product.get(pk)

    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }


@app.get("/products")
def all():
    return [format(pk) for pk in Product.all_pks()]


@app.post("/products")
def create(product: Product):
    return product.save()


@app.get("/products/{pk}")
def get(pk: str):
    return Product.get(pk)


@app.delete("/products/{pk}")
def delete(pk: str):
    return Product.delete(pk)
