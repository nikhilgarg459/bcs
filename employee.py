#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Employee class
"""
from customers import Customer
class Employee:
	
	found_user=""

	def __init__(self, username,password):
		self.username = username 
		self.password = password

	def  add_Account(self,user,passw,money):
		self.update_Database(Customer(user,passw,money).toString(),"a+")
		return "Account added successfully!"

	def  delete_Account(self,user):	
		j=self.search_User(user)
		if(j==1):
			return "Account deleted successfully!"
		else:
			return "No user with username "+user	

	def change_Password(self,user,passw):			
		j=self.search_User(user)
		if(j==0):
			return "User "+user+" not found"
		else:
			p=found_user.split(' ')
			self.update_Database(Customer(user,passw,p[2]).toString(),"a+")
			return "Password change successfully!"
	
	def search_User(self,user):
		with open ("custom.txt", "r") as myfile:
			global found_user
			data=myfile.read()
			ar=data.split('\n')	
			hum= len(ar) - 1
			j=0
			for i in range(0,hum):
				ar1=ar[i].split(' ')
				if(ar1[0]==user):
					found_user=ar[i]
					ar.remove(ar[i])
					j=1
					break	
			if(j==1):
				s="\n"
				other_users=s.join(ar)
				self.update_Database(other_users.strip('\n'),'w')			
		return j
		
	def update_Database(self,users,attr):
		f=open('custom.txt',attr)
		f.write(users+"\n")
		f.close()
