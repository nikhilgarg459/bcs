#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Customer class
"""
from database import Database

class Customer:

	def __init__(self, username, password, money):
		self.username = username 
		self.password = password
		self.money = money

	def deposit(self, amount):
		datab = Database(self.username, self.password)
		j, found_user = datab.search_User(user)
		self.money += amount
		datab.update_Database(self.toString(), "a+")
		return "Money deposited successfully!"


	def withdraw(self, amount):
		if(self.money >= amount):
			self.money -= amount
			datab = Database(self.username, self.password)
			j, found_user = datab.search_User(user)
			datab.update_Database(self.toString(), "a+")
			return "Money withdrawn successfully!"
		else:
			print "Not enough money!"	

	def toString(self):
		return self.username + " " + self.password + " " + str(self.money)	

	def logout(self):
		datab = Database(self.username, self.password)
		datab.update_Database(self.toString(), "a+")	