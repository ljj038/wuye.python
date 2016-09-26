#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import pika
import json

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)


# 创建 Connection
amqpConnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 创建 Channel
amqpChannel = amqpConnection.channel()

# 创建一个指定名字的 queue
# why?
# 为了确保名字为 card_updata_info 的队列已经创建了
# productor 和 consumer 都需要 try to create the queue
sQueueName = 'card_updata_info'
amqpChannel.queue_declare(queue=sQueueName)

amqpChannel.basic_consume(consumer_callback=callback, queue=sQueueName, no_ack=True)
amqpChannel.start_consuming()
