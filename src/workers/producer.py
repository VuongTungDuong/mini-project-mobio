from confluent_kafka import Message, Producer

conf = {"bootstrap.servers": "localhost:9092"}


producer = Producer(conf)


def delivery_report(err, msg: Message):
    try:
        if err is not None:
            print(f"Message delivery failed {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
    except Exception as e:
        print(f"Error: {e}")


keys = ["key1", "key2", "key3", "key4", "key5"]

for i in range(100):
    producer.produce(
        "my-topic",
        key="key1",
        value=f"hello {i}",
        callback=delivery_report,
    )
    producer.poll(0)
producer.flush()
print("All messages produced")
