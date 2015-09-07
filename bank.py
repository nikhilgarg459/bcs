#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * This module has DataStore class which is serilazble.
"""

from config import DB_FILE
from datastore import SingletonDataStore

class Account:

    def __init__(self, name, email, password, account_type):
        self.name = name
        self.email = email
        self.password = password
        self.type = account_type
        self.money = 0

    def deposit(self, amount):
        self.money += amount
        return "Money deposit Succesfull! New Balance: " + str(self.money)

    def withDraw(self, amount):
        if amount <= self.money:
            self.money -= amount
            return "Money withdraw Succesfull! New Balance: " + str(self.money)
        return "Sorry you can withdraw max of Rs. " + str(self.money)
 
    def login(self, password):
        if password == self.password:
            return "Login Successful", self.type
        return "Wrong password", "None"      

    def changePassword(self, password):
            self.password = password
            return "Password change Successfully"

class Bank(SingletonDataStore):

    def __init__(self, filename):
        if self.initialized:
            return
        print "Bank DB initialized..."
        self.initialized = True
        super(Bank, self).__init__(filename=filename)
        self.accounts = dict()
        self.init()

    def addAccount(self, account):
        with self.__class__.__singleton_lock:
            if account.email in self.accounts:
                return "Email id already registered"
            self.accounts[account.email] = account
            self.save()
            return "Account added Successfully"

    def deleteAccount(self, email):
        with self.__class__.__singleton_lock:
            if email in self.accounts:
                del self.accounts[email]
                self.save()
                return "Account deleted Successfully"
            return "No account with this Email id"

    def withDraw(self, email, amount):
        with self.__class__.__singleton_lock:
            if email in self.accounts:
                return self.accounts[email].withDraw(amount)
                self.save()
            return None

    def deposit(self, email, amount):
        with self.__class__.__singleton_lock:
            if email in self.accounts:
                return self.accounts[email].deposit(amount)
                self.save()
            return None

    def login(self, email, password):
        with self.__class__.__singleton_lock:
            if email in self.accounts:
                print self.accounts[email].login(password)
                self.save()
            print "Wrong Username", "None"

    def changePassword(self, email, password):
         with self.__class__.__singleton_lock:
            if email in self.accounts:
                return self.accounts[email].changePassword(password)
                self.save()
            return "No account with this Email id"
                          

if __name__ == '__main__':

    obj1 = Bank(DB_FILE)
    obj2 = Bank(DB_FILE)
    #acc = Account("Nikhil", "nik72", "niks", "Employee")
    #obj1.addAccount(acc)
    print obj1 is obj2