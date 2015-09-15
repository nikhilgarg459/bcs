#!usr/bin/env python
# -*-coding:utf8-*-

import socket
from client_logger import setup_logging, getLogger

__doc__ = """
    * This module provides a general client class which can be extended to
      use in any application that involves sending messages using sockets.
"""


# Configuration
MESSAGE_LENGTH = 1024
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5010


class Client(object):

    def __init__(self, server_ip=SERVER_IP, server_port=SERVER_PORT):
        # It's a good practice to declare all object variables in init
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = None  # this was not declared
        self.port = None
        self.ip = None
        self.log = None

    def receive(self):
        msg = None
        try:
            msg = self.sock.recv(MESSAGE_LENGTH)
        except Exception as e:
            print "Error while receing message from server"
            raise e
        return msg

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        val = self.sock.connect((self.server_ip, self.server_port))
        self.ip, self.port = self.sock.getsockname()
        # Below method gives us server ip and port
        self.sock.getpeername()
        # Log files will be named by port numbers
        setup_logging(str(self.port))
        self.log = getLogger(str(self.port))
        self.log.info('Successfully connected to the server at %s:%s' %
                      (self.server_ip, self.server_port))

    def close_conn(self):
        self.log.info('Closing connection...')
        self.sock.close()

    def prompt(self, prompt_message):
        user_input = None
        try:
            user_input = raw_input(prompt_message).strip()
        except Exception as e:
            self.log.debug('Error while getting user input')
            raise e
        return user_input

    def send(self, msg):
        try:
            self.sock.send(msg)
        except Exception as e:
            self.log.debug('Error sending message:  %s' % msg)
            raise e
