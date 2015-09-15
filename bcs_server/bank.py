#!usr/bin/env python
# -*-coding:utf8-*-

from config import DB_FILE, ADMIN_NAME, ADMIN_EMAIL, ADMIN_PASSWORD
from datetime import datetime
from datastore import SingletonDataStore
from account import Account
from server_logger import log

__doc__ = """
    * This module has DataStore class which is serilazble.
"""


class Bank(SingletonDataStore):

    def __init__(self, filename=DB_FILE):
        if self.initialized:
            return
        log.info('Bank DB initialized...')
        self.initialized = True
        super(Bank, self).__init__(filename=filename)
        self.accounts = dict()
        self.accounts['admin@bcs.com'] = Account(ADMIN_NAME, ADMIN_EMAIL,
                                                 ADMIN_PASSWORD, 'Employee')
        self.init()
        self.logged_ins = dict()
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
            if email in self.logged_ins:
                return "Account cannot be deleted as user is currently online"
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
                if "Login Successful" in msg:
                    if email in self.logged_ins:
                        return "Login Unsuccessful! Mupltiple logins with\
                                same email id", "Invalid"
                    self.logged_ins[email] = self.accounts[
                                             email].datetime_now()
                return msg
            return "Login Unsuccessful", "Invalid"

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
                return msg
            return "No account with this Email id"

    def printLedger(self):
        print '\n', ' *** Accounts in Bank ***'.center(67, ' '), '\n'
        print '    %-15s %-20s  %-15s %-10s' % ('Name', 'Email',
                                                'Password', 'Account Type')
        print '    %-15s %-20s  %-15s %-10s' % ('----', '-----',
                                                '--------', '------------')
        for account in self.accounts.values():
            print '    ' + str(account)
        print '\n'

if __name__ == '__main__':
    Bank()
    print Bank().logged_ins
