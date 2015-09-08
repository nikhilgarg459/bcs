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
        self.money += int(amount)
        return "Money deposit Succesfull! New Balance Rs. " + str(self.money)

    def withDraw(self, amount):
        if int(amount) <= self.money:
            self.money -= int(amount)
            return "Money withdraw Succesfull! New Balance Rs. " + str(self.money)
        return "Sorry you can withdraw max of Rs. " + str(self.money)
 
    def login(self, password):
        if password == self.password:
            return "Login Successful", self.type
        return "Wrong password", "Invalid"      

    def changePassword(self, password):
            self.password = password
            return "Password change Successfully"

class Bank(SingletonDataStore):

    def __init__(self, filename=DB_FILE):
        if self.initialized:
            return
        print "Bank DB initialized..."
        self.initialized = True
        super(Bank, self).__init__(filename=filename)
        self.accounts = dict()
        self.init()

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
                return self.accounts[email].login(password)
            return "Wrong Username", "Non"

    def changePassword(self, email, password):
         with self.__class__._singleton_lock:
            if email in self.accounts:
                msg = self.accounts[email].changePassword(password)
                self.save()
                return msg
            return "No account with this Email id"
                          

#if __name__ == '__main__':

 #   obj1 = Bank()
    #obj2 = Bank(DB_FILE)
    #acc = Account("Nikhil", "nik72", "niks", "Employee")
    #acc = Account("Osho", "osh", "osh", "Customer")
    #obj1.addAccount(acc)
    #obj1.withDraw("aks", 500)
    #obj1.deposit("aks", 500)
    #print obj1 is obj2