#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
FOR ACCESSING DATABASE
"""
class Database:

	def search_User(self, user):
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
					ar.remove(ar[i])
					j = 1
					break	
			if j == 1:
				s = "\n"
				other_users = s.join(ar)
				self.update_Database(other_users.strip('\n'), 'w')			
		return j, found_user
		
	def update_Database(self, users, attr):
		f = open('custom.txt', attr)
		f.write(users + "\n")
		f.close()
