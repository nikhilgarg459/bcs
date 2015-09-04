#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * This module provide client class to access the bcs server.
    * This module can be run directly as follows to run as standalone client:

        > python client.py

    * Work in Progress *
"""

import socket
import time

# Configuration
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5008
MESSAGE_LENGTH = 1024


class Client:


    def __init__(self, server_ip=SERVER_IP, server_port=SERVER_PORT):
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

    def run(self):
        try:
            print self.receive()     #Welcome to bcs
            self.option()  #Username nikhil  #From emp.txt
            self.option()    #Password nikhil   #From emp.txt
            print self.receive()
            recvd = self.receive()
            if recvd == '1':                    #Login Successful
                while True:
                    recvd = self.receive()     #Get choices
                    self.send(recvd) #Select Choice
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
    client_app = Client()
    client_app.run()
