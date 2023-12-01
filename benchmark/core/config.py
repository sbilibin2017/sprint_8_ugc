from enum import Enum
from logging import config as logging_config

from dotenv import load_dotenv
from pydantic.fields import Field
from pydantic_settings import BaseSettings

from benchmark.core.logger import LOGGING

# Применяем настройки логирования
logging_config.dictConfig(LOGGING)
load_dotenv(".env.dev")


class Settings(BaseSettings):

    # Clickhouse
    CHUNK_SIZE: int = Field(1000, env="CHUNK_SIZE")
    clickhouse_host: str = Field('localhost', env="clickhouse_host")
    clickhouse_db_name: str = Field(..., env="clickhouse_db_name")
    clickhouse_table_name: str = Field(..., env="clickhouse_table_name")


class OlapProviders(str, Enum):
    CLICKHOUSE = "clickhouse"


def get_olap_providers():
    from benchmark.data_management.clickhouse import ClickhouseClient

    providers = {
        OlapProviders.CLICKHOUSE: ClickhouseClient
    }

    return providers


settings = Settings()
