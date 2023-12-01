import http
import json
import uuid

import tests.functional.utils.tokens as utils_tokens

USER_UUID = uuid.uuid4()
USER_UUID_STR = str(USER_UUID)
JWT_TOKEN = utils_tokens.create_correct_token(USER_UUID)
BAD_TOKENS = utils_tokens.create_all_bad_tokens(USER_UUID)

UGC_ADD_DATA = [
    (
        {
            "timestamp": 10000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "user_id": USER_UUID_STR,
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 20000,
            "payload": json.dumps(
                {
                    "action": "repost",
                    "user_id": USER_UUID_STR,
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 30000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "user_id": USER_UUID_STR,
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 40000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                    "user_id": USER_UUID_STR,
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 50000,
            "payload": json.dumps(
                {
                    "action": "repost",
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                    "user_id": USER_UUID_STR,
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
]

UGC_INVALID_UUID = [
    (
        {
            "timestamp": 10000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "movie_id": "invalid_uuid",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 20000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "user_id": "invalid_uuid",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 30000,
            "payload": json.dumps(
                {
                    "action": "like",
                    "movie_id": "invalid_uuid",
                    "user_id": USER_UUID_STR,
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 40000,
            "payload": json.dumps(
                {
                    "action": "repost",
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                    "user_id": "invalid_uuid",
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 50000,
            "payload": json.dumps(
                {
                    "action": "repost",
                    "movie_id": "invalid_uuid",
                    "user_id": "invalid_uuid",
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
]

UGC_INVALID_BODY = [
    (
        {
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "payload": json.dumps(
                {
                    "action": "like",
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "payload": json.dumps(
                {
                    "action": "like",
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 40000,
            "payload": json.dumps(
                {
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                    "user_id": USER_UUID_STR,
                    "any_parameter": "some_info",
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 50000,
            "payload": json.dumps({"any_parameter": "some_info"}),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 60000,
            "payload": json.dumps(
                {
                    "user_id": USER_UUID_STR,
                }
            ),
        },
        JWT_TOKEN,
    ),
    (
        {
            "timestamp": 70000,
            "payload": json.dumps(
                {
                    "movie_id": "50919feb-bcf3-43e4-9728-208f9209b9ef",
                }
            ),
        },
        JWT_TOKEN,
    ),
]

UGC_INVALID_TOKEN = [
    (
        {
            "timestamp": 10000,
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        BAD_TOKENS[0],
        http.HTTPStatus.FORBIDDEN,
    ),
    (
        {
            "timestamp": 20000,
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        BAD_TOKENS[1],
        http.HTTPStatus.UNAUTHORIZED,
    ),
    (
        {
            "timestamp": 30000,
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        BAD_TOKENS[2],
        http.HTTPStatus.UNAUTHORIZED,
    ),
    (
        {
            "timestamp": 40000,
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        BAD_TOKENS[3],
        http.HTTPStatus.UNAUTHORIZED,
    ),
    (
        {
            "timestamp": 50000,
            "payload": json.dumps(
                {
                    "action": "like",
                }
            ),
        },
        BAD_TOKENS[4],
        http.HTTPStatus.UNAUTHORIZED,
    ),
]
