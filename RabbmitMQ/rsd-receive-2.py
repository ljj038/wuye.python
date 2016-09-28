#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'
import pika
import time

print ' [*] Waiting for messages. To exit press CTRL+C'


def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep(30)
    ch.basic_ack(delivery_tag=method.delivery_tag)


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

# no_ack=True  消息被 Consumer 接收到后 不管是否被处理完成 Broker server 都会将该消息在 Queue 中删除
# no_ack=False  默认 消息被 Consumer 接收到后 Consumer 会在处理完成后发送 act 告知 Broker server 将该消息在 Queue 中删除
amqpChannel.basic_consume(consumer_callback=callback, queue=sQueueName, no_ack=False)
amqpChannel.start_consuming()
