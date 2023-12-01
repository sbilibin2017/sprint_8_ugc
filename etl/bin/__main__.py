import logging
import os

import libs.app as app
import libs.etl as etl

logger = logging.getLogger(__name__)


def run() -> None:
    settings = app.get_settings()
    kafka_servers = [f"{settings.kafka_host}:{settings.kafka_port}"]
    try:
        etl.run_etl(kafka_servers, settings.kafka_topics, settings.kafka_group)
    except Exception as err:
        logger.error(err)


def main():
    try:
        run()
        exit(os.EX_OK)
    except SystemExit:
        exit(os.EX_OK)
    # except app.ApplicationError:
    #     exit(os.EX_SOFTWARE)
    except KeyboardInterrupt:
        logger.info("Exited with keyboard interrupt")
        exit(os.EX_OK)
    except BaseException:
        logger.exception("Unexpected error")
        exit(os.EX_SOFTWARE)


if __name__ == "__main__":
    main()
