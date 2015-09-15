#!usr/bin/env python
# -*-coding:utf8-*-

import socket
import thread
from config import MESSAGE_LENGTH, TCP_IP, TCP_PORT, MAX_CONNECTIONS
from server_logger import log

__doc__ = """
            This module provides a general server class which can be
            extended to use in any application that involves sending
            messages using sockets.
"""


class Server(object):

    def __init__(self):
        self.count = 0

    def start(self):
        pass

    def respond(self, client, msg, parameters):
        log.debug('msg: %s' % msg)
        log.debug('Parameters: %s' % parameters)
        if parameters is None:
            parameters = ""
        client.send(str(msg + "~" + parameters))

    def receive(self, conn, addr):
        msg = None
        try:
            msg = conn.recv(MESSAGE_LENGTH)
            log.debug(msg)
            msg, params = msg.split("~")
            parameters = self.extractParams(params)
        except Exception as e:
            log.error('Error while receiving message from %s' % addr)
            log.error(e)
            raise e
        return msg, parameters

    def extractParams(self, params):
        parameters = dict()
        if params != "":
            paramArray = params.split(',')
            for param in paramArray:
                key, value = param.split('=')
                parameters[key] = value
            return parameters
        return None

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Following line prevents this: socket.error:
        # [Errno 48] Address already in use
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((TCP_IP, TCP_PORT))
        sock.listen(1)
        log.info('Listening for connections...')
        while 1:
            # Accept connection from client.
            conn, addr = sock.accept()
            address = '%s:%s' % addr
            log.info('Connection request from %s' % address)
            if self.count == MAX_CONNECTIONS:
                log.info('Max connections reached, request denied...')
                conn.send("Server Busy,Try again Later~type=invalid")
                conn.close()
            else:
                log.info('Request accepted, connecting...')
                self.count += 1
                thread.start_new_thread(self.start, (conn, address))
        sock.close()
