'''
Primary Author: Kent Pawson
Contributor(s): Azita Saleh
'''

from domain import Password
from database import connect
import mysql.connector
from encryption import Encryption

class ModifyPasswordModel:
    def __init__(self):
        pass
    
    def _update_password_in_database(self, password: Password, original_title: str) -> bool:
        result = True

        website_title = password.get_title()
        url = password.get_url()
        username = password.get_username()
        _password = password.get_password()
        encryption = Encryption(_password)
        encrypted_pass = encryption.apply_cipher()

        try:
            # Connect to DB, set cursor
            cxn = connect()
            cursor = cxn.cursor()

            # Query to update the Password's title, url, username, and password
            update_passwords_query = "UPDATE Passwords SET website_title = %s, url = %s, username = %s, encrypted_pass = %s WHERE website_title = %s"
            pass_values = (website_title, url, username, encrypted_pass, original_title)

            cursor.execute(update_passwords_query, pass_values)
            cxn.commit()
        except mysql.connector.Error as error:
            print(f"oopsie!", error)
            result = False
        finally:
            cursor.close()
            cxn.close()
        
        return result