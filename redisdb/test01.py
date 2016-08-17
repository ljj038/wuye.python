#!/usr/bin/python
# coding=utf-8
# redis
import redis
conn = redis.StrictRedis(host='localhost', port=6379, db=10)
print(conn.set('test_key', 100))
print(conn.get('test_key'))
