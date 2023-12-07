from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Microservice"
    host: str = "0.0.0.0"
    port: int = 8000
    password: str = "password"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
