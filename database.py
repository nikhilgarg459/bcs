#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
FOR ACCESSING DATABASE
"""
class Database:

	def read_Database(self, user):
		with open ("custom.txt", "r") as myfile:
			found_user = None
			data = myfile.read()
			ar = data.split('\n')	
			hum = len(ar) - 1
			j = 0
			for i in range(0, hum):
				ar1 = ar[i].split(' ')
				if ar1[0] == user:
					found_user = ar[i]
					j = 1
					break				
		return j, found_user ,ar

	def getUserName(self, user):
			userdetail = user.split(' ')
			return userdetail[0]

	def add_User(self, user):
		j, found_user ,ar = self.read_Database(self.getUserName(user))
		if j == 0:
			self.write_Database(user, "a+")
			return 1
		return 0	
					
		
	def search_User(self, user):
		j, found_user ,ar = self.read_Database(user)			
		return j, found_user

	def delete_User(self, user):
		j, found_user, ar = self.read_Database(user)
		if j == 1:
				ar.remove(found_user)
				s = "\n"
				other_users = s.join(ar)
				self.write_Database(other_users.strip('\n'), 'w')
		return j		
	
	def update_User(self, user):
		j = self.delete_User(self.getUserName(user))
		if j == 1:
			self.write_Database(user, "a+")
		
			
	def write_Database(self, users, attr):
		f = open('custom.txt', attr)
		f.write(users + "\n")
		f.close()
