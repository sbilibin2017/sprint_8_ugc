from pathlib import Path

from dotenv import dotenv_values
from pydantic import BaseConfig

ROOT = Path().parent.parent

config = dotenv_values(ROOT / '.env')


class Config(BaseConfig):
    ch_client_host:str=config['CLICKHOUSE_CLIENT_HOST']
    ch_server_port:int=int(config['CLICKHOUSE_SERVER_PORT'])
    ch_client_port:int=int(config['CLICKHOUSE_CLIENT_PORT'])    
    chunk_size:int=int(config['CHUNK_SIZE'])
    sleep:int=int(config['SLEEP'])
    n_users:int=int(config['N_USERS'])
    seed:int=int(config['SEED'])


config = Config()
