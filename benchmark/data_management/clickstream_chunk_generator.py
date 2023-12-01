import json
import random
import warnings

from uuid import uuid4

from benchmark.shemas.entity import Entry
from benchmark.core.config import settings

warnings.filterwarnings('ignore')


class PayloadGenerator:
    def __init__(self, chunk_size: int = None, actions: list = None):
        if chunk_size is None:
            self.CHUNK_SIZE = settings.CHUNK_SIZE
        else:
            self.CHUNK_SIZE = chunk_size
        if actions is None:
            self.ACTIONS = [
                'start_watch',
                'stop_watch',
                'continue_watch',
                'like',
                'dislike',
                'comment',
                'add_to_favorite',
                'delete_from_favorite',
                'user_device',
                'user_login',
                'user_logout'
            ]
        else:
            self.ACTIONS = actions

    @staticmethod
    def _generate_payload(actions):
        return json.dumps(
            {
                "id": uuid4().hex,
                "action": random.choice(actions),
                "params": "some_value",
            }
        )

    def get_all_generated_payloads(self, actions: list = None, chunk_size: int = None):
        if not actions:
            actions = self.ACTIONS
        if chunk_size is None:
            chunk_size = self.CHUNK_SIZE
        return [self._generate_payload(actions) for _ in range(chunk_size)]


def get_payloads():
    payload_generator = PayloadGenerator()
    payloads = payload_generator.get_all_generated_payloads()
    return [Entry(timestamp=random.randint(a=0, b=1e8), payload=json_payload) for json_payload in payloads]
