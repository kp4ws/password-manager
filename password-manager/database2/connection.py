"""
Author: Azita Saleh

Connects to MySQL database and updates it with user-provided websites and passwords,

Must be in the same dir as:

db.sql
config.json

"""

import mysql.connector
import json
import os

"""
	This function is connects to the database using the credentials defined in a config file.
	:return Connection object
"""
def connect():
	# Open the config file to retrieve login credentials
	with open('./database2/config.json') as f:
		config = json.load(f)

	# Connection string
	cxn = mysql.connector.connect(
		username=config['username'],
		password=config['password'],
		host=config['host'],
		database=config['database']
	)
	return cxn
"""
	This function inserts the password and title into the Passwords table and Websites table
	:pass_id The password id generated in the Passwords table
	:encrypted_pass The encrypted password
	:title The title of the website the user provided
	:hashed_pass The hashed version of the password
"""

	
def add_pass(encrypted_pass: str) -> None:


	# Connect to DB, set cursor
	cxn = connect()
	cursor = cxn.cursor()

	"""
	try:
		#
		# cxn.commit()
	except mysql.connector.Error as error:
		print(f"oopsie!", error)
	finally:
		cursor.close()
		cxn.close()
	"""

if __name__ == "__main__":
	connect()