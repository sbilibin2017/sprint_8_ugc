import logging

import kafka

import libs.app as app
import libs.etl as etl

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def run_etl(servers: list[str], topics: list[str], group: str) -> None:
    """Run ETL from Kafka to Clickhouse."""

    settings = app.get_settings()
    ch_client = etl.get_clickhouse_client()
    try:
        etl.init_db(ch_client)

        consumer = etl.get_kafka_consumer(servers, group)
        consumer.subscribe(topics)

        messages = []
        options = {}
        for message in consumer:
            messages.append(message)

            # Manual offset for kafka
            tp = kafka.TopicPartition(message.topic, message.partition)
            options[tp] = kafka.OffsetAndMetadata(message.offset + 1, None)

            logger.info("Message received: `%s`", message.value)
            logger.info("Messages Size: `%s`", len(messages))
            logger.info("Messages partition: `%s`", message.partition)
            logger.info("Topic: `%s", message.topic)
            if len(messages) >= settings.chunk_size:
                try:
                    transformed_data = etl.transform(messages)
                    etl.load(ch_client, transformed_data)
                    logger.info(f"Kafka Commit's Options: {options}")
                    consumer.commit(options)
                    messages = []
                    options = {}
                except Exception:
                    logger.exception("Unable to tranform and load data")
    finally:
        ch_client.close()
