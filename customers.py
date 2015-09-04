#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Customer class
"""
from database import Database

class Customer:

	def __init__(self, username, password, money, typ):
		self.username = username 
		self.password = password
		self.money = int(money)
		self.typ = typ

	def deposit(self, amount):
		datab = Database()
		self.money += amount
		datab.update_User(self.toString())
		return "Money deposited successfully!"

	def check_Balance(self):
		return "Rs. " + str(self.money)	

	def withdraw(self, amount):
		if(self.money >= amount):
			self.money -= amount
			datab = Database()
			datab.update_User(self.toString())
			return "Money withdrawn successfully!"
		else:
			return "You can withdraw maximum " + str(self.money)	

	def toString(self):
		return self.username + " " + self.password + " " + str(self.money)	+ " " + self.typ
		