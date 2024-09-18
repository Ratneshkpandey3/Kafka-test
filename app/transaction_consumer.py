from kafka import KafkaConsumer
import json
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

consumer = KafkaConsumer(
    'my-topic',
    bootstrap_servers=['kafka:9093'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)


conn = psycopg2.connect(
    dbname='transactions',
    user='user',
    password='password',
    host='postgres',
    port=5432
)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT NOT NULL,
    type VARCHAR(10) NOT NULL,
    timestamp FLOAT NOT NULL,
    user_id INT NOT NULL           
)
""")
conn.commit()

for message in consumer:
    transaction = message.value
    logging.info(f"Received transaction: {transaction}")

    cursor.execute("""
    INSERT INTO transactions (amount, type, timestamp, user_id)
    VALUES (%s, %s, %s, %s)
    """, (transaction['amount'], transaction['type'], transaction['timestamp'], transaction['user_id']))
    conn.commit()

cursor.close()
conn.close()
