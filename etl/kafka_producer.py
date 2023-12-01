import json

import kafka

producer = kafka.KafkaProducer(bootstrap_servers=["kafka:29092"])
# for i in range(2):
for y in range(6):
    json_entry = {"message": "New super number", "value": y}
    entry = json.dumps(json_entry)
    producer.send("like", bytes(entry, encoding="utf-8"))

producer.flush()
