#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Customer class
"""
class Customer:
	def __init__(self, username,password,money):
		self.username = username 
		self.password = password
		self.money = money

	def deposit(self,amount):
		money+=amount

	def withdraw(self,amount):
		if(money>=amount):
			money-=amount
		else:
			print "Not enough money!"	

	def toString(self):
		return self.username+" "+self.password+" "+str(self.money)+"\n"		