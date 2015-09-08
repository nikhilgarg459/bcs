#!usr/bin/env python
#-*-coding:utf8-*-

from bank import Bank
from bank import Account

__doc__  =  """
    * This module provides a general server class which can be extended to
       use in any application that involves sending messages using sockets.
"""

import socket

# Configuration
MESSAGE_LENGTH = 1024

class Server(object):

	def receive(self):
	    msg = None
	    try:
	        msg = self.client.recv(MESSAGE_LENGTH)
	        msg, params = msg.split(":")
	        parameters = self.getParam(params)
	    except Exception as e:
	        print "Error while receing message from server"
	        raise e
	    return msg, parameters

	def getParam(self, params):
		parameters = dict()
		if params != "":
		    paramArray = params.split(',')
		    for param in paramArray:
		        key, value = param.split('=')
		        parameters[key] = value
		    return parameters
		return ""    

	def setClient(self, client):
		self.client = client		

	def login(self, parameters):    
	    msg, typ = Bank().login(parameters['email'],parameters['password'])
	    self.respond(msg, str("type=" + typ))
	    return parameters['email'], msg
	    
	def addAccount(self, parameters):
	    msg = Bank().addAccount(Account(parameters['name'], parameters['email'], parameters['password'], parameters['type'])) 
	    self.respond(msg, "")

	def deleteAccount(self, parameters):
	    msg = Bank().deleteAccount(parameters['email'])
	    self.respond(msg, "")

	def changePassword(self, parameters):
	    msg = Bank().changePassword(parameters['email'], parameters['password']) 
	    self.respond(msg, "")
	    
	def logout(self):
	    self.respond("Logout Successful", "")
	    self.client.close()

	def deposit(self, email, parameters):
	    msg = Bank().deposit(email, parameters['amount'])
	    self.respond(msg, "")

	def withdraw(self, email, parameters):
	    msg = Bank().withDraw(email, parameters['amount'])
	    self.respond(msg, "")

	def respond(self, msg, parameters):
	    self.client.send(str(msg + ":" + parameters))