import logging
import typing

import backoff
import clickhouse_connect.driver.client
import clickhouse_connect.driver.exceptions

import libs.app as app

logger = logging.getLogger(__name__)


@backoff.on_exception(
    backoff.expo,
    clickhouse_connect.driver.exceptions.ClickHouseError,
    base=2,
    factor=1,
    max_value=60,
    max_tries=None,
)
def load(
    client: clickhouse_connect.driver.client.Client, data: list[list[typing.Any]]
) -> None:
    """Load data into Clickhouse ."""
    logger.info("Loading data into Clickhouse")

    settings = app.get_settings()
    columns = ["event_id", "action", "payload", "timestamp"]
    try:
        client.insert(
            f"{settings.db_name}.{settings.table_name}", data, column_names=columns
        )
    except Exception as e:
        logger.exception(f"Error while loading data into Clickhouse: {e}")
        raise e
