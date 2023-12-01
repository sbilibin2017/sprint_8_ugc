import logging
import typing
import uuid

import orjson

logger = logging.getLogger(__name__)


def transform(messages: list) -> list[list[typing.Any]]:
    """
    Transform data from Kafka to Clickhouse.

        :param messages: list of messages from Kafka
        :return: list[uuid, json as str, timestamp] to insert into Clickhouse
    """
    logger.info("Transforming data from Kafka to Clickhouse")
    data = []

    for message in messages:
        payload = orjson.dumps(message.value).decode("utf-8")
        entry = [uuid.uuid4(), message.topic, payload, message.timestamp]

        data.append(entry)

    return data
