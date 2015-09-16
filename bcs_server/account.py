#!usr/bin/env python
# -*-coding:utf8-*-

from datetime import datetime
from server_logger import log

__doc__ = """

        * Account class

"""


class Account:

    def __init__(self, name, email, password, account_type):
        self.name = name
        self.email = email
        self.password = password
        self.type = account_type
        self.money = 0
        self.passbook = []

    def datetime_now(self):
        """
            For format reference of datetime, refer to table at
            the end of following page:
            https://docs.python.org/2/library/datetime.html
        """
        datetime_now = datetime.now().strftime('%b %d, %Y %I:%M %p')
        return datetime_now

    def deposit(self, amount):
        self.money += int(amount)
        tx = (self.datetime_now(), amount, 0)
        self.passbook.append(tx)
        return "Money deposit Succesfull! New Balance Rs. " + str(self.money)

    def withDraw(self, amount):
        if int(amount) <= self.money:
            self.money -= int(amount)
            tx = (self.datetime_now(), 0, amount)
            self.passbook.append(tx)
            return "Money withdraw Succesfull! New Balance Rs. " + str(self.money)
        return "Sorry you can withdraw max of Rs. " + str(self.money)

    def login(self, password):
        if password == self.password:
            return "Login Successful", self.type
        return "Login Unsuccessful", "Invalid"

    def changePassword(self, password):
            self.password = password
            return "Password change Successfully"

    def getPassbook(self):
        if len(self.passbook) == 0:
            return 'No transactions'
        return '\n'.join(['%s  :  %s  :  %s' % (tx[0], tx[1], tx[2])
                          for tx in self.passbook])

    def __str__(self):
        return '%-15s %-20s  %-15s %-10s' % (self.name, self.email,
                                             self.password, self.type)
