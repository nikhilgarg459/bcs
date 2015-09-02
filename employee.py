#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Employee class
"""
from customers import Customer
from database import Database

class Employee:

	def __init__(self, username, password):
		self.username = username 
		self.password = password

	def  add_Account(self, user, passw, money):
		datab = Database(self.username, self.password)
		datab.update_Database(Customer(user, passw, money).toString(), "a+")
		return "Account added successfully!"

	def  delete_Account(self, user):
		datab = Database(self.username, self.password)	
		j, found_user = datab.search_User(user)
		if j == 1 :
			return "Account deleted successfully!"
		else:
			return "No user with username " + user	

	def change_Password(self, user, passw):
		datab = Database(self.username, self.password)			
		j, found_user = datab.search_User(user)
		if j == 0 :
			return "User " + user + " not found"
		else:
			p = found_user.split(' ')
			datab.update_Database(Customer(user, passw, p[2]).toString(), "a+")
			return "Password change successfully!"
	
	
