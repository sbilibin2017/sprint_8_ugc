import clickhouse_driver

from benchmark.data_management.base_client import BaseDBClient
from benchmark.core.config import settings
from benchmark.data_management import clickstream_chunk_generator
from benchmark.shemas.entity import Entry


class ClickhouseClient(BaseDBClient):
    def __init__(self):
        self.client: clickhouse_driver.Client = None
        self.db_name = settings.clickhouse_db_name
        self.db_table = settings.clickhouse_table_name

    def connect(self, **kwargs) -> clickhouse_driver.Client:
        self.client = clickhouse_driver.Client(host=settings.clickhouse_host)
        return self.client

    def disconnect(self):
        self.client.disconnect()

    def create_db(self):
        self.client.execute(f'CREATE DATABASE IF NOT EXISTS {self.db_name} ON CLUSTER company_cluster')

    def create_table(self):
        self.client.execute(f'CREATE TABLE IF NOT EXISTS {self.db_name}.{self.db_table} '
                            'ON CLUSTER company_cluster (id String, timestamp Int64, action String,  params String) '
                            'Engine=MergeTree() '
                            'ORDER BY id')

    def drop_database(self):
        self.client.execute(f'DROP DATABASE IF EXISTS {self.db_name};')

    @BaseDBClient.timing_decorator
    def load_data(self, limit: int):
        total_load = 0
        while total_load < limit:
            payloads: list[Entry] = clickstream_chunk_generator.get_payloads()
            entries = [entry.dict() for entry in payloads]

            self.client.execute(
                f'INSERT INTO {self.db_name}.{self.db_table} (timestamp, id, action, params) VALUES',
                [(entry['timestamp'], entry['payload']['id'], entry['payload']['action'], entry['payload']['params'])
                 for entry in entries]
            )
            total_load += len(payloads)

    @BaseDBClient.timing_decorator
    def select_data(self, data: dict = None, start_timestamp: int = None, end_timestamp: int = None):
        params = []
        if data:
            params = [f"`{key}` = '{value}'" for key, value in data.items()]
        if start_timestamp:
            params.append(f"`timestamp` > {start_timestamp}")
        if end_timestamp:
            params.append(f"`timestamp` < {end_timestamp}")
        query = f'SELECT COUNT(*) FROM {self.db_name}.{self.db_table} WHERE {" AND ".join(params)}'
        return self.client.execute(query)[0][0]

    def clear_table(self):
        self.client.execute(f'TRUNCATE TABLE  {self.db_name}.{self.db_table}')

    def execute_query(self, query):
        return self.client.execute(query)

    @BaseDBClient.timing_decorator
    def get_count(self):
        return self.client.execute(f'SELECT COUNT(*) FROM {self.db_name}.{self.db_table}')[0][0]
