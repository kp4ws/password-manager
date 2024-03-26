from domain import Password
from encryption import Encryption
from database import connect
import mysql.connector

class CreatePasswordModel:
    def __init__(self):
        pass

    def _save_password_to_database(self, password: Password) -> None:
        
        website_title = password.get_title()
        url = password.get_url()
        username = password.get_username()
        encrypted_pass = password.get_password()
        #TODO: encrypted_pass = encrypt(password)
        date_created = password.get_created_date()
        
        print(username)

        try:
            # Connect to DB, set cursor
            cxn = connect()
            cursor = cxn.cursor()

            # Query to insert the title and password to the Passwords table
            insert_into_passwords_query = "INSERT INTO Passwords (website_title, url, username, encrypted_pass, date_created) VALUES (%s, %s, %s, %s, %s)"
            pass_values = (website_title, url, username, encrypted_pass, date_created)
            cursor.execute(insert_into_passwords_query, pass_values)
            #cursor.excecute(insert_into_websites_query, sites_values)
            # Commits the two queries as one transcation
            cxn.commit()
        except mysql.connector.Error as error:
            print(f"oopsie!", error)
        finally:
            cursor.close()
            cxn.close()