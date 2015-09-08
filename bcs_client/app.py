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

# Configuration
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5010

class BcsClient(Client):

    def __init__(self, server_ip=SERVER_IP, server_port=SERVER_PORT):
        # Calling constructor(__init__) of parent class
        # @Nikhil we are passing child classname and child object(which is self) to super
        super(BcsClient, self).__init__(server_ip, server_port)
        self._session = None

    def run(self):
        try:
            user = self.login()
            
            if user['type'] == "Employee":
                while True:
                    choice = self.prompt("1 Add new Account\n2 Delete Account\n3 Change Password\n4 Logout\nPlease enter ypur choice: ")
                    if choice == '1':
                        self.addAccount()
                    elif choice == '2':
                        self.deleteAccount()
                    elif choice == '3':
                        self.changePassword()   
                    elif choice == '4':
                        self.logout()
                        break      
                    else:
                        print "Wrong choice" 

            elif user['type'] == "Customer":
                while True:
                    choice = self.prompt("1 Deposit\n2 Withdraw\n3 Logout\nPlease enter ypur choice: ")
                    if choice == '1':
                        self.deposit()
                    elif choice == '2':
                        self.withdraw()
                    elif choice == '3':
                        self.logout()
                        break
                    else:
                        print "Wrong choice"                     

        except Exception, e:
            print e.args
            self.sock.close()

if __name__ == '__main__':
    client_app = BcsClient()
    while True:    
        client_app.run()
        choice = client_app.prompt("Press 1 to exit: ")
        if choice == '1':
            break
