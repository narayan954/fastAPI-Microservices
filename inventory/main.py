from redis_om import get_redis_connection, HashModel
from fastapi import FastAPI
from config import settings
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

redis = get_redis_connection(
    host=settings.host,
    port=settings.port,
    password=settings.password,
    decode_responses=True,
)

class ProductIn(BaseModel):
    name: str
    price: float
    quantity: int

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


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/products")
def all():
    return [format(pk) for pk in Product.all_pks()]


@app.post("/products")
def create(product: ProductIn):
    new_product = Product(**product.model_dump())
    return new_product.save()


@app.get("/products/{pk}")
def get(pk: str):
    return Product.get(pk)


@app.delete("/products/{pk}")
def delete(pk: str):
    return Product.delete(pk)
