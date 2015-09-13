#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * This module has DataStore class which is serilazble.
"""

from config import DB_FILE, ADMIN_NAME, ADMIN_EMAIL, ADMIN_PASSWORD
from datastore import SingletonDataStore
from account import Account

class Bank(SingletonDataStore):

    def __init__(self, filename=DB_FILE):
        if self.initialized:
            return
        print "Bank DB initialized..."
        self.initialized = True
        super(Bank, self).__init__(filename=filename)
        self.accounts = dict()
        self.accounts['admin@bcs.com'] = Account(ADMIN_NAME, ADMIN_EMAIL, ADMIN_PASSWORD, 'Employee')
        self.init()
        self.printLedger()

    def addAccount(self, account):
        with self.__class__._singleton_lock:
            if account.email in self.accounts:
                return "Email id already registered"
            self.accounts[account.email] = account
            self.save()
            return "Account added Successfully"

    def deleteAccount(self, email):
        with self.__class__._singleton_lock:
            if email in self.accounts:
                del self.accounts[email]
                self.save()
                return "Account deleted Successfully"
            return "No account with this Email id"

    def withDraw(self, email, amount):
        with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].withDraw(amount)
                self.save()
                return msg
            return "Transaction failed"

    def deposit(self, email, amount):
        with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].deposit(amount)
                self.save()
                return msg
            return "Transaction failed"

    def login(self, email, password):
        with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].login(password)
                self.save()
                return msg
            return "Login Unsuccessful", "Non"

    def changePassword(self, email, password):
         with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].changePassword(password)
                self.save()
                return msg
            return "No account with this Email id"
    
    def getPassbook(self, email):
        with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].getPassbook()
                self.save() # why do we need this ? This is a read operation
                return msg
            return "No account with this Email id"                          

    def printLedger(self):
        print 'Accounts in Bank:'
        print '----------------'
        for account in self.accounts.values():
            print '    ' + str(account)
        print '\n'

if __name__ == '__main__':
     Bank()
 #   obj1 = Bank()
    #obj2 = Bank(DB_FILE)
    #acc = Account("Nikhil", "nik72", "niks", "Employee")
    #acc = Account("Osho", "osh", "osh", "Customer")
    #obj1.addAccount(acc)
    #obj1.withDraw("aks", 500)
    #obj1.deposit("aks", 500)
    #print obj1 is obj2