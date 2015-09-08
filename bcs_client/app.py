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
SERVER_PORT = 5010

class BcsClient(Client):

    def __init__(self, server_ip=SERVER_IP, server_port=SERVER_PORT):
        # Calling constructor(__init__) of parent class
        # @Nikhil we are passing child classname and child object(which is self) to super
        super(BcsClient, self).__init__(server_ip, server_port)
        self._session = None

    def run(self):
        try:
            print "Welcome to BCS!"
            email = self.prompt("Email id: ")
            password = self.prompt("Password: ")
            self.request("authenticate", str("email=" + email + "," + "password=" + password))
            user = self.response()
            
            if user['type'] == "Employee":
                
                while True:
                    
                    choice = self.prompt("1 Add new Account\n2 Delete Account\n3 Change Password\n4 Logout\nPlease enter ypur choice: ")
                    
                    if choice == '1':
                        name = self.prompt("Enter Name: ")
                        email = self.prompt("Enter Email: ")
                        password = self.prompt("Enter Password: ")
                        typenum = self.prompt("Select Type 1.Employee 2.Customer: ")
                        typ = "Employee"
                        if typenum == '2':
                            typ = "Customer"
                        self.request("addAccount", str("name=" + name + "," + "email=" + email + "," + "password=" + password + "," + "type=" + typ))
                        self.response()

                    elif choice == '2':
                        email = self.prompt("Enter Email: ")
                        self.request("deleteAccount",str("email=" + email))
                        self.response()

                    elif choice == '3':
                        email = self.prompt("Enter Email: ")
                        password = self.prompt("Enter new Password: ")
                        self.request("changePassword", str("email=" + email + "," + "password=" + password))
                        self.response()

                    elif choice == '4':
                        self.request("logout", "")
                        self.response()
                        break      

                    else:
                        print "Wrong choice" 

            elif user['type'] == "Customer":

                while True:
                    
                    choice = self.prompt("1 Deposit\n2 Withdraw\n3 Logout\nPlease enter ypur choice: ")
                    
                    if choice == '1':
                        amount = self.prompt("Enter amount: Rs. ")
                        self.request("deposit", str("amount=" + amount))
                        self.response()

                    elif choice == '2':
                        amount = self.prompt("Enter amount: Rs. ")
                        self.request("withdraw", str("amount=" + amount))
                        self.response()

                    elif choice == '3':
                        self.request("logout", "")
                        self.response()
                        break

                    else:
                        print "Wrong choice"                     

        except Exception, e:
            print e.args
        finally:
            self.sock.close()


if __name__ == '__main__':
    client_app = BcsClient()
    client_app.run()
