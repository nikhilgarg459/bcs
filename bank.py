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

    def withDraw(self, amount):
        if amount <= self.money:
            self.money -= amount
            return amount
        return None


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
                return 0
            self.accounts[account.email] = account
            self.save()
            return 1

    def deleteAccount(self, email):
        with self.__class__.__singleton_lock:
            if email in self.accounts:
                del self.accounts[email]
                self.save()
                return 1
            return 0

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


if __name__ == '__main__':

    obj1 = Bank(DB_FILE)
    obj2 = Bank(DB_FILE)

    print obj1 is obj2
