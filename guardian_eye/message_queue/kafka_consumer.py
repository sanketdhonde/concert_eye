import json
from kafka import KafkaConsumer
import logging

logging.basicConfig(level=logging.INFO)

class KafkaMessageConsumer:
    def __init__(self, topic, bootstrap_servers='localhost:9092'):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='guardian-eye-group',
            value_deserializer=lambda m: json.loads(m.decode('utf-8'))
        )

    def consume_messages(self):
        for message in self.consumer:
            logging.info(f'Consumed message: {message.value}')
            yield message.value

    def close(self):
        self.consumer.close()

if __name__ == '__main__':
    consumer = KafkaMessageConsumer('alerts_topic')
    for msg in consumer.consume_messages():
        print(msg)