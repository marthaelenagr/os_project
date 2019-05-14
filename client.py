#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
from json import dumps

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine ip and assign port
host = socket.gethostname()
port = 9999

# connection to hostname on the port.
s.connect((host, port))
messages = [(0.0, 'RealMemory 2'), (0.1, 'SwapMemory 4'), (0.2, 'PageSize 16'),
            (0.3, 'PolíticaMemory LRM y MRM'), (1, 'P 2048 1'), (2, 'A 1 1 0'),
            (3, 'A 33 1 1'), (4, 'P 32 2'), (5, 'A 15 2 0'), (6, 'A 82 1 0'),
            (7, 'L 2'), (8, 'P 32 3'),  (9, 'L 1'),  (10, 'F'),  (11,  'E')]

# Wait for message to be received from the server
response = s.recv(1024).decode('utf-8')
print(response)

for msg in messages:
    s.send(dumps([msg[0], msg[1]]).encode('utf-8'))

    print(s.recv(1024).decode('utf-8'))
