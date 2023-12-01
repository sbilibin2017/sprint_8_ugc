import dataclasses

import aiohttp
import multidict
import pytest_asyncio

import tests.config as config


@dataclasses.dataclass
class HTTPResponse:
    body: dict | str
    headers: multidict.CIMultiDictProxy[str]
    status_code: int


@pytest_asyncio.fixture
async def http_client():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture
def make_event_request(http_client):
    async def inner(
        url: str = config.tests_settings.get_ugc_url(),
        body: dict | None = None,
        jwt_token: dict | None = None,
    ) -> HTTPResponse:
        if body is None:
            body = {}
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {jwt_token}",
        }
        async with http_client.post(url, json=body, headers=headers) as response:
            return HTTPResponse(
                body=await response.json(),
                headers=response.headers,
                status_code=response.status,
            )

    return inner
