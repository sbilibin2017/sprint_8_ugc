import abc
import time
from functools import wraps

from benchmark.shemas.entity import QueryTimeResult


class BaseDBClient(abc.ABC):

    def timing_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            return QueryTimeResult(
                execute_time=format(end_time - start_time, '.2f'),
                execute_result=result
            )

        return wrapper

    @abc.abstractmethod
    def connect(self, **kwargs):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

    @abc.abstractmethod
    def create_db(self, **kwargs):
        pass

    @abc.abstractmethod
    def create_table(self, **kwargs):
        pass

    @abc.abstractmethod
    def drop_database(self):
        pass

    @abc.abstractmethod
    def load_data(self, limit: int):
        pass

    @abc.abstractmethod
    def select_data(self, data: dict, start_timestamp: int = None, end_timestamp: int = None):
        pass

    @abc.abstractmethod
    def clear_table(self):
        pass

    @abc.abstractmethod
    def execute_query(self, query):
        pass

    @abc.abstractmethod
    def get_count(self, **kwargs):
        pass
