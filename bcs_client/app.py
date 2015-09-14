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
import sys


# Add logging instead of print wherever print is not being used for CLI

class BcsClient(Client):

    def __init__(self):
        super(BcsClient, self).__init__()
        self._session = None

    def run(self):
        try:
            user = self.login()
            
            if user['type'] == "Employee":
                while True:
                    employee_options = ['Add Account', 'Delete Account', 'Change Password', 'Logout']
                    choice = self.prompt(self.genMenu(employee_options))
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
                    customer_options = ['Deposit', 'Withdraw', 'Passbook', 'Logout']
                    choice = self.prompt(self.genMenu(customer_options))
                    if choice == '1':
                        self.deposit()
                    elif choice == '2':
                        self.withdraw()
                    elif choice == '3':
                        self.getPassbook()    
                    elif choice == '4':
                        self.logout()
                        break
                    else:
                        print "Wrong choice"                     

        except Exception, e:
            print e.args
            self.close_conn()

    def response(self): 
        reply = self.receive()
        msg, params = reply.split("~")
        print msg
        if params != "":
            parameters = self.getParam(params)
            return parameters
        return ""   

    def request(self, msg, parameters):  
        self.send(str(msg + "~" + parameters))

    def getParam(self, params):
        parameters = dict()
        paramArray = params.split(',')
        for param in paramArray:
            key, value = param.split('=')
            parameters[key] = value
        return parameters    
    
    def genMenu(self, options):
        menu = '\n'.join(['%d. %s' % (index+1, item) for index,item in enumerate(options)])        
        return menu + "\nEnter your Choice: "

    def login(self):
        self.email = self.prompt("Email id: ")
        self.password = self.prompt("Password: ")
        self.connect()
        connection = self.response()
        if connection['type'] == "valid":
            self.request("authenticate", str("email=" + self.email + "," + "password=" + self.password))
            user = self.response()
            return user
        self.close_conn()    
        return connection    

    def getPassbook(self):        
        self.request("getPassbook", str("email=" + self.email))
        print "         Date And Time : Credit : Debit"
        self.response()

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
        self.close_conn()   

    def deposit(self):                
        self.transact("deposit") 

    def withdraw(self):
        self.transact("withdraw")        
    
    def transact(self, typ):
        amount = self.prompt("Enter amount: Rs. ")
        self.request(typ, str("amount=" + amount + "," + "email=" + self.email))
        self.response()            

if __name__ == '__main__':
    client_app = BcsClient()
    while True:
            try:
                client_app.run()
                choice = client_app.prompt("Press 1 to exit: ")
                if choice == '1':
                    break
            except KeyboardInterrupt:
                pass
            finally:
                print 'Keyboard Interupt, logout and closing connection..'
                client_app.logout()
                sys.exit(0)
