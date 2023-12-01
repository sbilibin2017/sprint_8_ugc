import clickhouse_connect.driver.client

import libs.app as app


def init_db(client: clickhouse_connect.driver.client.Client) -> None:
    """Create database and table if not exists."""
    settings = app.get_settings()

    create_db = f"CREATE DATABASE IF NOT EXISTS {settings.db_name}"
    create_table = f"""CREATE TABLE IF NOT EXISTS {settings.db_name}.{settings.table_name}
    (
        `event_id` UUID,
        `action` String,
        `payload` String,
        `timestamp` DateTime64(3, 'UTC'),
    )
    ENGINE = MergeTree()
    PRIMARY KEY (event_id, timestamp)
    """

    client.command(create_db)
    client.command(create_table)
