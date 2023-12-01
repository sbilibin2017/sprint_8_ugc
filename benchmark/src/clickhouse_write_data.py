def clickhouse_write_data(clickhouse_client, records_to_insert):
    clickhouse_client.execute('INSERT INTO test (id, user_id, timestamp, payload) VALUES', records_to_insert)
