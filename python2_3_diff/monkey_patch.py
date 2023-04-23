#!/bin/env/python
# coding=utf-8
# gevent运行时替换socket属性等。
import socket

print(socket.socket)

print("import gevent socket...")

from gevent import socket


