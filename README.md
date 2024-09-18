# Kafka Test Setup

This Kafka test is a small setup to demonstrate how Kafka works in a real-life scenario. I have created two Python scripts:
- **Kafka Publisher**: This script generates random transactions every 2 seconds.
- **Kafka Consumer**: This script consumes those transactions.

Zookeeper is used to manage and ensure no loss of data, even in case of failures, with the help of Kafka's replication feature.

## Prerequisites
Before running the project, make sure Docker Desktop is running on your system.

## Running the Project

1. Start the Kafka and Zookeeper setup using Docker Compose:
    ```bash
    docker-compose up -d
    ```

2. Check that the containers are up and running:
    ```bash
    docker ps
    ```

3. In a separate terminal tab, run the Kafka consumer:
    ```bash
    docker exec -it kafka-docker-flask-app-1 python /transaction_consumer.py
    ```

4. In another terminal tab, run the Kafka producer:
    ```bash
    docker exec -it kafka-docker-flask-app-1 python /transaction_producer.py
    ```

## Viewing Results

Once the producer and consumer are running, you can check the data on [http://localhost:5000](http://localhost:5000).

