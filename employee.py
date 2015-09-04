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

	def  add_Account(self, user, passw, money, typ):
		datab = Database()
		j = datab.add_User(Customer(user, passw, money, typ).toString())
		if j == 1:
			return "Account added successfully!"
		return "Username aleready taken"

	def  delete_Account(self, user):	
		datab = Database()
		j = datab.delete_User(user)
		if j == 1 :
			return "Account deleted successfully!"
		else:
			return "No user with username " + user	

	def change_Password(self, user, passw):			
		datab = Database()
		j, found_user = datab.search_User(user)
		if j == 0 :
			return "User not found"
		else:
			p = found_user.split(' ')
			datab.update_User(Customer(user, passw, p[2], p[3]).toString())
			return "Password change successfully!"
	
	
