from random import randint
from time import sleep

from confluent_kafka import Consumer

group_id = input("Enter group id: ")

conf = {
    "bootstrap.servers": "localhost:9092",
    "group.id": group_id,
    "auto.offset.reset": "earliest",
}
consumer = Consumer(conf)
consumer.subscribe(["my-topic"])

try:
    while True:
        msg = consumer.poll(5)
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        print(
            f"Received {msg.key().decode() if msg.key() else 'None'}, value: {msg.value().decode('utf-8')}"
        )
        # Simulate processing time
        # 1-5 seconds
        sleep(randint(1, 5))

except Exception:
    print("Error occurred")
