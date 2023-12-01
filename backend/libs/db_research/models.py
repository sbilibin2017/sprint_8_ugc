import uuid

import pydantic


class PayloadModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="allow")

    action: str
    user_id: uuid.UUID | None = None
    movie_id: uuid.UUID | None = None

    def get_key(self):
        if self.movie_id:
            return f"{self.user_id}_{self.movie_id}"
        return self.user_id or self.movie_id

    @pydantic.field_serializer("user_id", "movie_id")
    def serialize_uuid(self, item_uuid: uuid.UUID | None):
        if not item_uuid:
            return item_uuid
        return item_uuid.hex


class Entry(pydantic.BaseModel):
    """
    Схема, используемая для представления записей, передаваемых в Producer.

    Атрибуты:
    - timestamp: Unix timestamp, представляющий время создания записи.
                 Должен быть представлен в виде целого числа.
    - payload: Объект JSON, представляющий полезную нагрузку записи.
               Может быть любым JSON-совместимым объектом.
    """
    timestamp: int
    payload: pydantic.Json[PayloadModel]


class Event(pydantic.BaseModel):
    event: Entry
    topic: str
    key: uuid.UUID | str | None

    @pydantic.field_serializer("key")
    def serialize_uuid(self, item_uuid: uuid.UUID | str | None):
        if not item_uuid or not isinstance(item_uuid, uuid.UUID):
            return item_uuid
        return item_uuid.hex


class Token(pydantic.BaseModel):
    sub: uuid.UUID
    exp: int = None
