from kafka import KafkaProducer
import json

def send_order(order_data):
    producer = KafkaProducer(
        bootstrap_servers='localhost:9094',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    
    producer.send('order_topic', order_data)
    producer.flush()
    print("Order sent:", order_data)

if __name__ == "__main__":
    order_example = {
        'order_id': 123,
        'product_id': 456,
        'quantity': 2,
        'price': 19.99
    }
    send_order(order_example)
