from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers=['kafka:9093'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:
    transaction = {
        'amount': round(random.uniform(10.0, 100.0), 2),
        'type': random.choice(['credit', 'debit']),
        'timestamp': time.time(),
        'user_id': random.randint(1,20)
    }
    producer.send('my-topic', value=transaction)
    print(f"Produced: {transaction}")
    time.sleep(5)
