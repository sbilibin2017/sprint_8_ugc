import functools

import clickhouse_connect
import clickhouse_connect.driver.client as ch_client
import clickhouse_connect.driver.exceptions
import kafka

import libs.app as app


@functools.lru_cache
def get_clickhouse_client() -> ch_client.Client:
    """Get Clickhouse client."""

    settings = app.get_settings()

    return clickhouse_connect.get_client(
        host=settings.db_host,
        port=settings.db_port,
        username=settings.db_user,
        password=settings.db_password,
    )


def get_kafka_consumer(servers: list[str], group: str) -> kafka.KafkaConsumer:
    """Get Kafka consumer."""
    consumer = kafka.KafkaConsumer(
        bootstrap_servers=servers,
        auto_offset_reset="earliest",
        enable_auto_commit=False,
        group_id=group,
        value_deserializer=lambda x: x.decode("utf-8"),
    )
    return consumer
