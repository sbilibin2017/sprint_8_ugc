import json

import aiokafka
import backoff
from aiokafka import AIOKafkaProducer

from libs.db_research.models import Event


@backoff.on_exception(
    backoff.expo,
    aiokafka.errors.KafkaConnectionError,
    base=2,
    factor=1,
    max_value=60,
    max_tries=None
)
async def send(event: Event, producer: AIOKafkaProducer):
    event_dict = event.model_dump()
    message = json.dumps(event_dict).encode("utf-8")
    if key := event_dict.get("key"):
        key = key.encode("utf-8")
    await producer.send(event.topic, value=message, key=key)
