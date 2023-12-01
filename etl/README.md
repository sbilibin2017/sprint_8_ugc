# ETL: Kafka -> ClickHouse

## Install & Run

1. Configure a ClickHouse cluster:
    - Modify `users.xml` for admin and user parameters.
    - Adjust `config.xml` for cluster settings (currently 1 shard - 2 replicas).
    - Execute `cd etl && make config` to generate configuration files.

2. Create a `.env` file based on the `.env.example` and complete it with the necessary values.

3. Launch your Kafka cluster. If you're running it locally, ensure it's accessible within the Docker network.

4. Run `docker-compose up -d` to initiate the cluster and the ETL process.

## Notes

1. Running `make config` resets your ClickHouse cluster settings. If you wish to retain your current configurations, you can omit this step and utilize the `config.xml` file as a guide to manually update your cluster.

2. You might opt to directly configure Kafka settings and topics in the `settings.py` file.

3. Take into account the option of utilizing `make lint-fix` to automatically rectify any encountered linting errors.
