from domain import Password
from database import connect
import mysql.connector
from encryption import Encryption

class CreatePasswordModel:
    def __init__(self):
        pass

    def _save_password_to_database(self, password: Password) -> bool:
        result = True

        website_title = password.get_title()
        url = password.get_url()
        username = password.get_username()
        _password = password.get_password()
        encryption = Encryption(_password)
        encrypted_pass = encryption.apply_cipher()
        
        date_created = password.get_created_date()

        try:
            # Connect to DB, set cursor
            cxn = connect()
            cursor = cxn.cursor()

            # Query to insert the title and password to the Passwords table
            insert_into_passwords_query = "INSERT INTO Passwords (website_title, url, username, encrypted_pass, date_created) VALUES (%s, %s, %s, %s, %s)"
            pass_values = (website_title, url, username, encrypted_pass, date_created)
            
            cursor.execute(insert_into_passwords_query, pass_values)
            cxn.commit()
        except mysql.connector.Error as error:
            print(f"oopsie!", error)
            result = False
        finally:
            cursor.close()
            cxn.close()
        
        return result