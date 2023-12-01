from libs.db_research.models import Entry, Event
from libs.db_research.repositories import producer_manager


async def send(data: Entry, producer):
    topic = data.payload.action
    key = data.payload.get_key()

    await producer_manager.send(
        Event(
            event=data,
            topic=topic,
            key=key,
        ),
        producer,
    )
