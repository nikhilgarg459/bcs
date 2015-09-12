#!usr/bin/env python
#-*-coding:utf8-*-

from serv import BcsServer

__doc__ = """
This class provide server side access to application.
"""

import socket
import thread

TCP_IP = '127.0.0.1'
TCP_PORT = 5010
MAX_CONNECTIONS = 2

class Server(BcsServer):

    def __init__(self):
        # Calling constructor(__init__) of parent class
        self.count = 0
        super(Server, self).__init__()

    def start(self, client, addr):
        #self.setClient(client)    
        self.respond(client, "Welcome to Bcs",str("type=valid"))    
        print "Accepted connection from: ", addr
        try:
            email = None
            while True:
                msg, parameters = self.receive(client)
                if msg == "authenticate":
                    email, msg = self.login(client, parameters)
                    if msg != "Login Successful":
                        break
                elif msg == "addAccount":
                    self.addAccount(client, parameters)
                elif msg == "deleteAccount":
                    self.deleteAccount(client, parameters)    
                elif msg == "changePassword":
                    self.changePassword(client, parameters)            
                elif msg == "withdraw":
                    self.withdraw(client, email, parameters)
                elif msg == "deposit":
                    self.deposit(client, email, parameters) 
                elif msg == "getPassbook":
                    self.getPassbook(client, email)       
                elif msg == "logout":  
                    self.logout(client)
                    break

                
        except Exception,e:
            print e.args
            print "Error after menu " + str(addr)
        finally:  
            self.count -= 1  
            client.close()
         

    def connect(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((TCP_IP, TCP_PORT))
        sock.listen(1)
        while 1:
            #while self.count > MAX_CONNECTIONS - 1:
             #   pass
            client, addr = sock.accept()     # Establish connection with client.
            self.count += 1
            if self.count > MAX_CONNECTIONS:
                client.send("Server Busy,Try again Later:type=invalid")
                self.count -= 1
                client.close()
            else:
                thread.start_new_thread(self.start, (client, addr))
        sock.close()

if __name__ == '__main__':
    server_app = Server()
    server_app.connect()

