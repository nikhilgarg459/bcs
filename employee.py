#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
Employee class
"""
from customers import Customer
class Employee:
	found_user=""
	other_users=""
	def __init__(self, username,password):
		self.username = username 
		self.password = password

	def  add_Account(self):
		user=raw_input("Create username: ")
		passw=raw_input("Create password: ")
		money=int(input("Intial money: Rs"))
		c=Customer(user,passw,money)
		self.update_Database(c.toString(),"a+")
		print "Account added successfully!"

	def  delete_Account(self,user):	
			j=self.search_User(user)
			if(j==1):
				self.update_Database(other_users.strip('\n')+"\n","w")
				print "Account deleted successfully!"
			else:
				print "No user with username "+user	

	def change_Password(self,user):			
		j=self.search_User(user)
		if(j==0):
			print "User "+user+" not found"
		else:
			passw=raw_input("Create password: ")
			p=found_user.split(' ')
			self.update_Database(other_users.strip('\n')+"\n"+user+" "+passw+" "+p[2]+"\n",'w')
	
	def search_User(self,user):
		with open ("custom.txt", "r") as myfile:
			global found_user
			global other_users
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
		return j
		
	def update_Database(self,users,attr):
		f=open('custom.txt',attr)
		f.write(users)
		f.close()

e=Employee("niks","nik")
#e.add_Account()
#e.delete_Account("Arnav")
#e.change_pPassword("ankur")