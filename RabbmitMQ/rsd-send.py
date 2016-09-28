#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'

import pika

# 创建 Connection
amqpConnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 创建 Channel
amqpChannel = amqpConnection.channel()

# 创建一个指定名字的 queue
sQueueName = 'card_updata_info'
# 为了保证在 RabbitMQ 退出或者 crash 了数据仍没有丢失，需要将 Queue 和 Message 都要持久化
# Queue 持久化
amqpChannel.queue_declare(queue=sQueueName, durable=True)

# 终端可以使用 rabbitmqctl list_queues 命令去验证名字为 card_updata_info 的队列是否创建成功

# Producer 只能发送到 exchange 它是不能直接发送到 queue 的
# 使用默认的 exchange 允许我们发送给指定的 queue 的名字
# body 就是 payload 即实际的消息内容

for i in range(1, 11):
    sMessage = 'hello:%s' % i
    print sMessage
    # Message 持久化
    amqpChannel.basic_publish(exchange='', routing_key=sQueueName, body=sMessage, properties=pika.BasicProperties(delivery_mode=2))

# 关闭连接
amqpConnection.close()
