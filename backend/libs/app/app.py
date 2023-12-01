import logging
import logging.config as logging_config

import aiokafka.producer
import backoff
import fastapi
import uvicorn

from aiokafka import AIOKafkaProducer as Producer

from libs import db_research

from .logger import LOGGING
from .settings import get_settings


logging_config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


class Application:
    def __init__(self) -> None:
        self.settings = get_settings()
        self.logger = logging.getLogger(__name__)
        self.producer = None

    def create_app(self) -> fastapi.FastAPI:
        app = fastapi.FastAPI(
            title=self.settings.project_name,
            description=self.settings.project_description,
            version=self.settings.project_version,
            docs_url="/api/openapi",
            openapi_url="/api/openapi.json",
            default_response_class=fastapi.responses.ORJSONResponse,
        )

        app.include_router(db_research.handlers.events.router, prefix='/api/v1/events', tags=['events'])

        @app.on_event("startup")
        @backoff.on_exception(backoff.expo, aiokafka.errors.KafkaConnectionError, base=2, factor=1,
                              max_value=60, max_tries=None)
        async def startup_event():
            self.logger.info("Starting server")

            self.producer = Producer(bootstrap_servers=f'{self.settings.kafka_host}:{self.settings.kafka_port}')
            await self.producer.start()
            app.state.producer = self.producer

        @app.on_event("shutdown")
        async def shutdown_event():
            await self.producer.stop()
            self.logger.info("Shutting down server")

        return app


__all__ = ["Application"]
