import logging
import pika

logger = logging.getLogger(__name__)

logger.info("Starting application")

def send(exchange="shard"):

    connection = getConnection()
    channel = connection.channel()
    channel.exchange_declare(exchange, "direct")

    for val in range(50):
        val_str = str(val)
        queue_name = f"queue-{val}"
        channel.queue_declare(queue=queue_name, arguments={"x-queue-type": "quorum"})
        channel.queue_bind(queue_name, exchange, val_str)

    send_items(exchange, channel)

    print(" [x] Sent 'Hello World!'")
    connection.close()


def send_items(exchange, channel):
    for message in range(10000):
        channel.basic_publish(exchange=exchange, routing_key=str(message % 50), body=f"Hello World! {message}")
    channel.close()


def getConnection():
    connection = pika.BlockingConnection(
        [
            pika.ConnectionParameters(host='rabbitmq-consul-1'),
            pika.ConnectionParameters(host='rabbitmq-consul-2'),
            pika.ConnectionParameters(host='rabbitmq-consul-3'),
        ]
    )
    return connection


if __name__ == '__main__':
    send(exchange="shard")
