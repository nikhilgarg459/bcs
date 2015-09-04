#!usr/bin/env python
#-*-coding:utf8-*-

from client import Client

__doc__  =  """
    * This module provide client-app class to access the bcs server. This extends the Client class.
    * This module can be run directly as follows to run as standalone client:

        > python app.py

    * Work in Progress *
    -> Add messaging protocol between server and client
    -> Shift CLI(Command-Line-Interface) logic to client
"""

import socket
import time

# Configuration
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5008

class BcsClient(Client):

    def __init__(self, server_ip=SERVER_IP, server_port=SERVER_PORT):
        # Calling constructor(__init__) of parent class
        # @Nikhil we are passing child classname and child object(which is self) to super
        super(BcsClient, self).__init__(server_ip, server_port)
        self._session = None

    def run(self):
        try:
            print self.receive()     #Welcome to bcs
            self.option()  #Username nikhil  #From emp.txt
            self.option()    #Password nikhil   #From emp.txt
            print self.receive()
            recvd = self.receive()
            if recvd == '1':                    #Login Successful
                while True:
                    self.option()    #Get choices
                    recvd = self.receive()
                    if recvd == '4':
                        self.option() #Create Userid:
                        self.option() #Create Password:
                        self.option()  #Intial money: Rs
                        self.option()  #Intial money: Rs   I don't understand this part
                        print self.receive()        #Account added successfully! # Added in custom.txt
                    elif recvd == '2':
                        self.option() #Userid #Any Userid from custom.txt
                        self.option()   #New Password:
                        print self.receive()         #Password change successfully! || No user with username #in custom.txt
                    elif recvd == '1':
                        self.option() #Userid to be deleted: # from custom.txt  #Enter amount:
                        print self.receive()        #Account deleted successfully!" || User not found in custom.txt
                    elif recvd == '6':
                        print self.receive()         #Logout Successful  #Check Balance
                        break
                    else:
                        print self.receive()         #Wrong Choice!

        except Exception, e:
            print e.args
        finally:
            self.sock.close()


if __name__ == '__main__':
    client_app = BcsClient()
    client_app.run()
