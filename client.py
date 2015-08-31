#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
This class provide client side access to application.
"""
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close 