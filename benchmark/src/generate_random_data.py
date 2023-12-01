import uuid

import numpy as np
import pandas as pd
from config import config
from dotenv import dotenv_values
from faker import Faker

Faker.seed(config.seed)
faker = Faker()

ACTIONS = [
    'start_watch',
    'stop_watch',
    'continue_watch',
    'like',
    'dislike',
    'comment',
    'add_to_favorite',
    'delete_from_favorite',  
    'user_login',
    'user_logout'
]

USER_IDS = [str(faker.uuid4()) for _ in range(config.n_users)]


def generate_random_data(chunk_size):
    ids        = np.array([uuid.uuid4().hex for _ in range(chunk_size)])
    user_ids   = np.random.choice(USER_IDS, size=chunk_size) 
    timestamps = np.int32(np.rint(np.random.uniform(0, 1e6, size=chunk_size)))
    actions    = np.random.choice(ACTIONS, size=chunk_size)
    data       = np.column_stack([ids, user_ids, timestamps, actions])
    df         = pd.DataFrame(data=data, columns=['id', 'user_id', 'timestamp','action'])
    del data 
    df['id']        = df['id'].astype('str')
    df['user_id']   = df['user_id'].astype('str')
    df['timestamp'] = df['timestamp'].astype('int')
    df['action']    = df['action'].astype('str')
    data = list(df.itertuples(index=False, name=None))
    del df
    return data
