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
        super(Bank, self).__init__(filename)
        self.accounts = dict()
        self.save()

    def addAccount(self, account):
        with cls.__singleton_lock:
            if account.email in self.accounts:
                return 0
            self.accounts[account.email] = account
            self.save()
            return 1

    def deleteAccount(self, email):
        with cls.__singleton_lock:
            if email in self.accounts:
                del self.accounts[email]
                self.save()
                return 1
            return 0

    def accessAccount(self, email):
        with cls.__singleton_lock:
            if email in self.accounts:
                return self.accounts[email]
            return None


def bank():
    return Bank.instance(DB_FILE)

if __name__ == '__main__':

    objmain = Bank(DB_FILE)
    obj1 = Bank.instance(DB_FILE)
    obj2 = Bank.instance(DB_FILE)

    print obj1 is obj2
    print objmain is obj1
    print objmain is obj2

