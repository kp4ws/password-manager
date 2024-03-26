'''
Primary Author: Azita Saleh
Contributor(s): N/A

Defines a function that connects to the MySQL database.

Must be in the same dir as:

db.sql
config.json
'''

import mysql.connector
import json
import os

def connect():
	'''
	This function is connects to the database using the credentials defined in a config file.
	:return Connection object
	'''
	cxn = None
	try:
		# Open the config file to retrieve login credentials
		with open('./database/config.json') as f:
			config = json.load(f)

		# Connection string
		cxn = mysql.connector.connect(
			username=config['username'],
			password=config['password'],
			host=config['host'],
			database=config['database']
		)
	except Exception as e:
		print(f'Error occured: {e}')
	
	return cxn