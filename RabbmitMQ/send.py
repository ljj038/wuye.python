#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhaoyingnan'

import pika
import json

# 创建 Connection
amqpConnection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

# 创建 Channel
amqpChannel = amqpConnection.channel()

# 创建一个指定名字的 queue
sQueueName = 'card_updata_info'
amqpChannel.queue_declare(queue=sQueueName)

# 终端可以使用 rabbitmqctl list_queues 命令去验证名字为 card_updata_info 的队列是否创建成功

# Producer 只能发送到 exchange 它是不能直接发送到 queue 的
# 使用默认的 exchange 允许我们发送给指定的 queue 的名字
# body 就是 payload 即实际的消息内容
dictMessage = {
    'update': {'class_id': 100137969, 'class_name': '智慧一班', 'school_id': 100025367},
    'condition': {'person_id': 61358, 'card_type': 1}
}
sMessage = json.dumps(dictMessage)
print amqpChannel.basic_publish(exchange='', routing_key=sQueueName, body=sMessage)

# 关闭连接
amqpConnection.close()

