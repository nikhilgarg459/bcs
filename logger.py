#!usr/bin/env python
#-*-coding:utf8-*-
__doc__ = """
FOR Log
"""
from database import Database

class Logger:
	def check_Credentials(self, user, pasw):
		datab = Database()
		j, found_user = datab.search_User(user)
		if j == 1:
			userdetails = found_user.split(' ')
			if pasw == userdetails[1]:
				return 1, userdetails[2], userdetails[3]
		return 0, None		
		