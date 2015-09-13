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

from server import Server


class BcsServer(Server):

    def __init__(self):
        super(BcsServer, self).__init__()

    def start(self, client, addr):
        #self.setClient(client)
        self.respond(client, "Welcome to Bcs",str("type=valid"))    
        print "Accepted connection from: ", addr
        try:
            #email = None
            while True:
                request_message, request_params = self.receive(client)
                # Get response message and parameters
                response_params = None
                response_msg = None
                if request_message == "authenticate":
                    response_msg, account_type = Bank().login(request_params['email'],request_params['password'])
                    response_params = str("type=" + account_type)
                elif request_message == "logout":
                    response_msg = "Logout Successful"
                else:
                    response_msg, response_params = self.bank_operation(request_message, request_params)
                # Respond to client
                self.respond(client, response_msg, response_params)
                # Close connection if authentication failed or logout
                if "Login Unsuccessful" in response_msg or response_msg == "Logout Successful":
                    client.close()
                    break
        except Exception,e:
            print e.args
            print "Error after menu " + str(addr)
        finally:  
            self.count -= 1  
            client.close()

    def bank_operation(self, request_message, request_params):
        response_msg = None
        response_params = None
        if request_message == "addAccount":
            response_msg = Bank().addAccount(Account(request_params['name'], request_params['email'], 
                                             request_params['password'], request_params['type']))
        elif request_message == "deleteAccount":
            response_msg = Bank().deleteAccount(request_params['email'])   
        elif request_message == "changePassword":
            response_msg = Bank().changePassword(request_params['email'], request_params['password'])          
        elif request_message == "withdraw":
            print 'withDraw: %s' % str(request_params)
            response_msg = Bank().withDraw(request_params['email'], request_params['amount'])
        elif request_message == "deposit":
            response_msg = Bank().deposit(request_params['email'], request_params['amount'])
        elif request_message == "getPassbook":
            response_msg = Bank().getPassbook(request_params['email'])  
        return response_msg, response_params

if __name__ == '__main__':
    server_app = BcsServer()
    server_app.connect()