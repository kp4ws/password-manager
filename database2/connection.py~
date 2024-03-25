"""
Author: Azita Saleh

Connects to MySQL database and updates it with user-provided websites and passwords,

Must be in the same dir as:

db.sql
config.json

"""

import mysql.connector
import json


"""
	This function is connects to the database using the credentials defined in a config file.
	:return Connection object
"""
def connect():

	# Open the config file to retrieve login credentials
	with open('config.json') as f:
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
	
	# Query to insert the title and password to the Passwords table
	insert_into_passwords_query = "INSERT INTO Passwords (encrypted_pass) VALUES (%s)"
	pass_values = (encrypted_pass)
	
	
	# Insert the title and hashed password into Websites
	#insert_into_websites_query = "INSERT INTO Websites (title, hashed_pass) VALUES (%s, %s)	
	#sites_values = (title, hashed_pass)
	
	try:
		cursor.execute(insert_into_passwords_query, pass_values)
		#cursor.excecute(insert_into_websites_query, sites_values)
		# Commits the two queries as one transcation
		cxn.commit()
	except mysql.connector.Error as error:
		print(f"oopsie!", error)
	finally:
		cursor.close()
		cxn.close()
	
if __name__ == '__main__':

	# For whatever reason, you have to pass in strings as lists for VARCHARS
	#add_pass(encrypted_pass=['A32F'])
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
