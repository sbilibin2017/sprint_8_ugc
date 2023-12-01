import functools

import pydantic
import pydantic_settings


class Settings(pydantic_settings.BaseSettings):
    """Settings."""

    project_name: str = pydantic.Field(default="DDD Temaplate", alias="PROJECT_NAME")
    project_description: str = pydantic.Field(
        default="Project description", alias="PROJECT_DESCRIPTION"
    )
    project_version: str = pydantic.Field(default="1.0.0", alias="PROJECT_VERSION")

    db_host: str = pydantic.Field(default="localhost", alias="DB_HOST")
    db_port: int = pydantic.Field(default=8123, alias="DB_PORT")
    db_user: str = pydantic.Field(default="admin", alias="DB_USER")
    db_password: str = pydantic.Field(default="123", alias="DB_PASSWORD")
    db_name: str = pydantic.Field(default="ugc_sprint_db", alias="DB_NAME")
    table_name: str = pydantic.Field(default="ugc_sprint_table", alias="TABLE_NAME")

    kafka_host: str = pydantic.Field(default="localhost", alias="KAFKA_INTERNAL_HOST")
    kafka_port: int = pydantic.Field(default=29092, alias="KAFKA_EXTERNAL_PORT")
    kafka_topics: list[str] = pydantic.Field(
        default=[
            "start_watch",
            "stop_watch",
            "continue_watch",
            "like",
            "dislike",
            "comment",
            "add_to_favorite",
            "delete_from_favorite",
            "user_login",
            "user_logout",
        ]
    )
    kafka_group: str = pydantic.Field(default="my-group", alias="KAFKA_GROUP")

    chunk_size: int = pydantic.Field(default=10000, alias="CHUNK_SIZE")

    model_config = pydantic_settings.SettingsConfigDict(env_file="./.env")


@functools.lru_cache
def get_settings() -> Settings:
    """Get settings."""
    return Settings()
