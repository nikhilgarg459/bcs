#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * This module provides a general client class which can be extended to
       use in any application that involves sending messages using sockets.
"""

import socket

# Configuration
MESSAGE_LENGTH = 1024

class Client(object):

    def __init__(self, server_ip, server_port):
        print "Welcome to BCS!"
        self.server_ip = server_ip
        self.server_port = server_port

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
        except Exception as e:
            print "Error sending message:  %s" % msg
            raise e

    def request(self, msg, parameters):  
        self.send(str(msg + ":" + parameters))

    def getParam(self, params):
        parameters = dict()
        paramArray = params.split(',')
        for param in paramArray:
            key, value = param.split('=')
            parameters[key] = value
        return parameters    

    def response(self): 
        reply = self.receive()
        msg, params = reply.split(":")
        print msg
        if params != "":
            parameters = self.getParam(params)
            return parameters
        return ""    
        
    def login(self):
        email = self.prompt("Email id: ")
        password = self.prompt("Password: ")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.server_ip, self.server_port))
        self.request("authenticate", str("email=" + email + "," + "password=" + password))
        user = self.response()
        return user

    def addAccount(self):
        name = self.prompt("Enter Name: ")
        email = self.prompt("Enter Email: ")
        password = self.prompt("Enter Password: ")
        typenum = self.prompt("Select Type 1.Employee 2.Customer: ")
        typ = "Employee"
        if typenum == '2':
            typ = "Customer"
        self.request("addAccount", str("name=" + name + "," + "email=" + email + "," + "password=" + password + "," + "type=" + typ))
        self.response()    

    def deleteAccount(self):
        email = self.prompt("Enter Email: ")
        self.request("deleteAccount",str("email=" + email))
        self.response()    

    def changePassword(self):
        email = self.prompt("Enter Email: ")
        password = self.prompt("Enter new Password: ")
        self.request("changePassword", str("email=" + email + "," + "password=" + password))
        self.response()    

    def logout(self):
        self.request("logout", "")
        self.response()
        self.sock.close()    

    def deposit(self):                
        self.transact("deposit") 

    def withdraw(self):
        self.transact("withdraw")        
    
    def transact(self, typ):
        amount = self.prompt("Enter amount: Rs. ")
        self.request(typ, str("amount=" + amount))
        self.response()
