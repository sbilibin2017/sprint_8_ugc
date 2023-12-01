import http

import pytest

import tests.functional.models as tests_models
import tests.functional.testdata as testdata

pytestmark = [pytest.mark.asyncio]


@pytest.mark.parametrize(
    "body,jwt_token",
    testdata.UGC_ADD_DATA,
)
async def test_ugc_add(
    body: tests_models.PayloadModel, jwt_token: str, make_event_request
):
    response = await make_event_request(body=body, jwt_token=jwt_token)
    assert response.status_code == http.HTTPStatus.CREATED


@pytest.mark.parametrize(
    "body,jwt_token",
    testdata.UGC_INVALID_UUID,
)
async def test_ugc_invalid_uuid(
    body: tests_models.PayloadModel, jwt_token: str, make_event_request
):
    response = await make_event_request(body=body, jwt_token=jwt_token)
    assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    "body,jwt_token",
    testdata.UGC_INVALID_BODY,
)
async def test_ugc_invalid_body(
    body: tests_models.PayloadModel, jwt_token: str, make_event_request
):
    response = await make_event_request(body=body, jwt_token=jwt_token)
    assert response.status_code == http.HTTPStatus.UNPROCESSABLE_ENTITY


@pytest.mark.parametrize(
    "body,jwt_token,error",
    testdata.UGC_INVALID_TOKEN,
)
async def test_ugc_invalid_token(
    body: tests_models.PayloadModel,
    jwt_token: str,
    error: http.HTTPStatus,
    make_event_request,
):
    response = await make_event_request(body=body, jwt_token=jwt_token)
    assert response.status_code == error
