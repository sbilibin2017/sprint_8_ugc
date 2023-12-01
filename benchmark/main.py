import time

from clickhouse_driver import Client
from config import config
from helpers.clickhouse_write_data import clickhouse_write_data
from helpers.generate_random_data import generate_random_data

clickhouse_client = Client(host=config.ch_client_host, port=config.ch_client_port)

while True:
    try:
        clickhouse_client.execute('CREATE TABLE IF NOT EXISTS test(id UUID, user_id UUID, timestamp Float32, payload String) ENGINE = Memory')
        data = generate_random_data(config.chunk_size)        
        clickhouse_write_data(clickhouse_client)
        time.sleep(config.sleep)
        del data
    finally:
        clickhouse_client.disconnect()
