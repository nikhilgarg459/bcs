#!usr/bin/env python
#-*-coding:utf8-*-

from serv import Server

__doc__ = """
This class provide server side access to application.
"""

import socket
import thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5010

class BcsServer(Server):

    def __init__(self):
        # Calling constructor(__init__) of parent class
        super(BcsServer, self).__init__()

    def start(self, client, addr):
        self.setClient(client)        
        print "Accepted connection from: ", addr
        try:
            email = None
            while True:
                msg, parameters = self.receive()
                if msg == "authenticate":
                    email, msg = self.login(parameters)
                    if msg != "Login Successful":
                        break
                elif msg == "addAccount":
                    self.addAccount(parameters)
                elif msg == "deleteAccount":
                    self.deleteAccount(parameters)    
                elif msg == "changePassword":
                    self.changePassword(parameters)            
                elif msg == "withdraw":
                    self.withdraw(email, parameters)
                elif msg == "deposit":
                    self.deposit(email, parameters)    
                elif msg == "logout":  
                    self.logout()
                    break

        except Exception,e:
            print e.args
            client.close()

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((TCP_IP, TCP_PORT))
        sock.listen(3)
        while 1:
            client, addr = sock.accept()     # Establish connection with client.
            thread.start_new_thread(self.start, (client, addr))
        sock.close()

if __name__ == '__main__':
    server_app = BcsServer()
    server_app.connect()

