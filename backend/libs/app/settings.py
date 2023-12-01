import functools

import pydantic
import pydantic_settings
from dotenv import load_dotenv
load_dotenv()


class Settings(pydantic_settings.BaseSettings):
    project_name: str = pydantic.Field(default="Research DB", alias="PROJECT_NAME")
    project_description: str = pydantic.Field(
        default="Research DB DDD ", alias="PROJECT_DESCRIPTION"
    )
    project_version: str = pydantic.Field(default="1.0.0", alias="PROJECT_VERSION")

    server_host: str = pydantic.Field(default="0.0.0.0", alias="SERVER_HOST")
    server_port: int = pydantic.Field(default=8000, alias="SERVER_PORT")

    kafka_host: str = pydantic.Field(default="127.0.0.1", alias="KAFKA_HOST")
    kafka_port: int = pydantic.Field(default=9092, alias="KAFKA_PORT")

    jwt_secret_key: str = pydantic.Field(..., alias="JWT_SECRET_KEY")
    jwt_algorithm: str = pydantic.Field("HS256", env="TOKEN_SIGN_ALGORITHM")


settings = Settings()


@functools.lru_cache
def get_settings() -> Settings:
    return Settings()
