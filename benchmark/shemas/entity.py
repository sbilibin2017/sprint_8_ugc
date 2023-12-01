import typing

import pydantic


class Entry(pydantic.BaseModel):
    timestamp: int
    payload: pydantic.Json[typing.Any]


class QueryTimeResult(pydantic.BaseModel):
    execute_time: float
    execute_result: typing.Any
