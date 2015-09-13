#!usr/bin/env python
#-*-coding:utf8-*-

__doc__ = """
This class provide server side access to application.
"""

import socket
import thread

from config import MESSAGE_LENGTH, TCP_IP, TCP_PORT, MAX_CONNECTIONS

class Server(object):

    def __init__(self):
        self.count = 0

    def start(self):
        pass

    def respond(self, client, msg, parameters):
        #print str("To client: " + msg + ":" + parameters)
        print 'msg: %s' % msg
        print 'Parameters: %s' % parameters
        if parameters == None:
            parameters = ""
        client.send(str(msg + "~" + parameters))

    def receive(self, client):
        msg = None
        try:
            msg = client.recv(MESSAGE_LENGTH)
            msg, params = msg.split("~")
            parameters = self.extractParams(params)
        except Exception as e:
            print "Error while receing message from client"
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

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Following line prevents this: socket.error: [Errno 48] Address already in use
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((TCP_IP, TCP_PORT))
        sock.listen(1)
        while 1:
            #while self.count > MAX_CONNECTIONS - 1:
             #   pass
            client, addr = sock.accept()     # Establish connection with client.
            self.count += 1
            if self.count > MAX_CONNECTIONS:
                client.send("Server Busy,Try again Later~type=invalid")
                self.count -= 1
                client.close()
            else:
                thread.start_new_thread(self.start, (client, addr))
        sock.close()
