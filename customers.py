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
		self.money = money
		self.typ = typ

	def deposit(self, amount):
		datab = Database()
		j, found_user = datab.search_User(user)
		self.money += amount
		datab.update_User(self.toString())
		return "Money deposited successfully!"


	def withdraw(self, amount):
		if(self.money >= amount):
			self.money -= amount
			datab = Database()
			j, found_user = datab.search_User(user)
			datab.update_User(self.toString())
			return "Money withdrawn successfully!"
		else:
			print "Not enough money!"	

	def toString(self):
		return self.username + " " + self.password + " " + str(self.money)	+ " " + self.typ
	def logout(self):
		datab = Database()
		datab.update_User(self.toString())	