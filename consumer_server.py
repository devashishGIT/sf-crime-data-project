import asyncio
import json
import random

from confluent_kafka import Consumer

async def consume(topic_name):
    """Consumes data from the Kafka Topic"""    
    c = Consumer({ "bootstrap.servers": "PLAINTEXT://localhost:9092", 
                   "group.id": "0",
                   "enable.auto.commit": "false",
                   "auto.offset.reset":"earliest"
                   })
    c.subscribe([topic_name])

    while True:
        messages = c.consume()
        for message in messages:
            print(f"consume message {message.key()}: {message.value().decode('utf-8')}")
        
        await asyncio.sleep(2)

def main():
    try:
        asyncio.run(consume("com.udacity.crime.data"))
        
    except KeyboardInterrupt as e:
        print("Stopping the Consumer")
    
if __name__ == "__main__":
    main()