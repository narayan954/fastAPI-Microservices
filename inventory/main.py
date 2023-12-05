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
