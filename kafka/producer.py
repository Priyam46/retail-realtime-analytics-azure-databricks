"""
Simulated POS Kafka producer.
Usage:
  pip install kafka-python
  docker-compose up -d   # if using the included docker-compose
  python kafka/producer.py
"""
import json
import uuid
import time
import random
from datetime import datetime, timezone
from kafka import KafkaProducer

BOOTSTRAP = "localhost:9092"
TOPIC = "retail.transactions"

products = ['P1','P2','P3','P4']
stores = ['S1','S2','S3']
payment_types = ['card','cash','digital']

def generate_event():
    return {
        "transaction_id": str(uuid.uuid4()),
        "store_id": random.choice(stores),
        "product_id": random.choice(products),
        "ts": datetime.now(timezone.utc).isoformat(),
        "quantity": random.randint(1,5),
        "price": round(random.uniform(0.5,50.0), 2),
        "payment_type": random.choice(payment_types),
        "loyalty_id": str(uuid.uuid4()) if random.random() > 0.6 else None
    }

def main():
    producer = KafkaProducer(
        bootstrap_servers=BOOTSTRAP,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print(f"Producing to {BOOTSTRAP} topic {TOPIC}")
    try:
        while True:
            evt = generate_event()
            producer.send(TOPIC, evt)
            print("sent:", evt)
            time.sleep(0.5)  # 2 events/sec
    except KeyboardInterrupt:
        print("stopping producer")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
