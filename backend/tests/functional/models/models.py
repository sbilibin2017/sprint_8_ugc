import uuid

import pydantic


class PayloadModel(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="allow")

    action: str
    user_id: uuid.UUID | None = None
    movie_id: uuid.UUID | None = None
