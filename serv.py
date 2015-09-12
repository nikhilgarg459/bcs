#!usr/bin/env python
#-*-coding:utf8-*-

from bank import Bank
from bank import Account

__doc__  =  """
    * This module provides a general server class which can be extended to
       use in any application that involves sending messages using sockets.
"""

import socket
import time
# Configuration
MESSAGE_LENGTH = 1024

class BcsServer(object):

	def receive(self, client):
	    msg = None
	    try:
	        msg = client.recv(MESSAGE_LENGTH)
	        #print "From Client: " + msg
	        #print msg
	        msg, params = msg.split(":")
	        parameters = self.getParam(params)
	    except Exception as e:
	        print "Error while receing message from client"
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

	def login(self, client, parameters):    
	    msg, typ = Bank().login(parameters['email'],parameters['password'])
	    self.respond(client, msg, str("type=" + typ))
	    return parameters['email'], msg
	    
	def addAccount(self, client, parameters):
	    msg = Bank().addAccount(Account(parameters['name'], parameters['email'], parameters['password'], parameters['type'])) 
	    self.respond(client, msg, "")

	def deleteAccount(self, client, parameters):
	    msg = Bank().deleteAccount(parameters['email'])
	    self.respond(client, msg, "")

	def changePassword(self, client, parameters):
	    msg = Bank().changePassword(parameters['email'], parameters['password']) 
	    self.respond(msg, "")
	    
	def logout(self, client):
	    self.respond(client, "Logout Successful", "")
	    client.close()

	def deposit(self, client, email, parameters):
	    msg = Bank().deposit(email, parameters['amount'])
	    self.respond(client, msg, "")

	def withdraw(self, client, email, parameters):
	    msg = Bank().withDraw(email, parameters['amount'])
	    self.respond(client, msg, "")

	def getPassbook(self, client, email):
		msg = Bank().getPassbook(email)
		self.respond(client, msg, "")

	def respond(self, client, msg, parameters):
		#print str("To client: " + msg + ":" + parameters)
		client.send(str(msg + ":" + parameters))