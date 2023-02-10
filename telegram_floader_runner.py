"""
Точка входа в приложение
"""
import pika
import time
import traceback
from main import main

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='work_d_out')


def callback(ch, method, properties, body):
    try:
        print("Started")
        main(body)
        print("Finished")
        time.sleep(60)
    except Exception:
        print(traceback.format_exc())


channel.basic_consume(on_message_callback=callback, queue='work_d_out', auto_ack=True)
print(' [*] Waiting for messages, press CTRL+C to exit')
channel.start_consuming()
