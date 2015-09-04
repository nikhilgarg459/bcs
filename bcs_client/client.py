#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * This module provides a general client class which can be extended to
       use in any application that involves sending messages using sockets.

    * Work in Progress *
    -> Remove 'sleep 1' from send method and do it in a 'proper' way.
"""

import socket
import time

# Configuration
MESSAGE_LENGTH = 1024

class Client(object):


    def __init__(self, server_ip, server_port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server_ip, server_port))

    def receive(self):
        msg = None
        try:
            msg = self.sock.recv(MESSAGE_LENGTH)
        except Exception as e:
            print "Error while receing message from server"
            raise e
        return msg

    def prompt(self, prompt_message):
        user_input = None
        try:
            user_input = raw_input(prompt_message).strip()
        except Exception as e:
            print "Error while getting user input"
            raise e
        return user_input

    def send(self, msg):
        try:
            self.sock.send(msg)
            time.sleep(1)
        except Exception as e:
            print "Error sending message:  %s" % msg
            raise e

    def option(self):
        prompt_message = self.receive()
        user_input = self.prompt(prompt_message)
        self.send(user_input)
