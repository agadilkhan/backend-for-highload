from kafka import KafkaConsumer
import json

def start_consumer():
    consumer = KafkaConsumer(
        'order_topic',
        bootstrap_servers='localhost:9094',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=True,
    )
    
    for message in consumer:
        order_data = message.value
        print(" [x] Received order data:", order_data)
        # Add your order processing logic here

if __name__ == "__main__":
    start_consumer()
