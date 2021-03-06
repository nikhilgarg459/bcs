#!usr/bin/env python
# -*-coding:utf8-*-

from bank import Bank
from bank import Account
import socket
import time
from server import Server
from server_logger import log

__doc__ = """
    * This module provide bcs_server class to access the bcs server.
    * This extends the Server class.
"""


class BcsServer(Server):

    def __init__(self):
        super(BcsServer, self).__init__()
        Bank()

    def start(self, conn, addr):
        self.respond(conn, "connecting...", str("type=valid"))
        log.info('Session started with %s' % addr)
        login_params = None
        debug = None
        try:
            while True:
                request_message, request_params = self.receive(conn, addr)
                # Get response message and parameters
                response_params = None
                response_msg = None
                debug = False
                log.info('Request from %s -  %s' % (addr, request_message))
                if request_message == "authenticate":
                    login_params = request_params
                    response_msg, account_type = Bank().login(
                                                 request_params['email'],
                                                 request_params['password'])
                    response_params = str("type=" + account_type)
                elif request_message == "logout":
                    response_msg = "Logout Successful"
                    del Bank().logged_ins[login_params['email']]
                else:
                    response_msg, response_params, debug = self.bank_operation(
                                                    request_message,
                                                    request_params)
                # Respond to client
                self.respond(conn, response_msg, response_params)
                if debug:
                    log.debug('Response to %s - %s' % (addr, response_msg))
                    log.info('Passbook sent to %s' % (addr))    
                else:
                    log.info('Response to %s - %s' % (addr, response_msg))
                # Close connection if authentication failed or logout
                if ("Login Unsuccessful" in response_msg or
                        response_msg == "Logout Successful"):
                    conn.close()
                    break
        except Exception as e:
            if login_params['email'] in Bank().logged_ins:
                del Bank().logged_ins[login_params['email']]
            log.error(e)
            log.error('Error after menu ' + str(addr))
        finally:
            self.count -= 1
            conn.close()

    def bank_operation(self, request_message, request_params):
        response_msg = None
        response_params = None
        debug = False
        if request_message == "addAccount":
            response_msg = Bank().addAccount(Account(request_params['name'],
                                             request_params['email'],
                                             request_params['password'],
                                             request_params['type']))
        elif request_message == "deleteAccount":
            response_msg = Bank().deleteAccount(request_params['email'])
        elif request_message == "changePassword":
            response_msg = Bank().changePassword(request_params['email'],
                                                 request_params['password'])
        elif request_message == "withdraw":
            log.debug('withDraw: %s' % str(request_params))
            response_msg = Bank().withDraw(request_params['email'],
                                           request_params['amount'])
        elif request_message == "deposit":
            response_msg = Bank().deposit(request_params['email'],
                                          request_params['amount'])
        elif request_message == "getPassbook":
            response_msg = Bank().getPassbook(request_params['email'])
            debug = True
        return response_msg, response_params, debug

if __name__ == '__main__':
    server_app = BcsServer()
    try:
        server_app.listen()
    except KeyboardInterrupt:
        log.info('Keyboard Interupt, Shutting down the server')
