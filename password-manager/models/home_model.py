from domain import Password
from database import connect
import mysql.connector
from encryption import Decryption

class HomeModel:
    '''
    Serves as the HomeModel for doing business logic associated with the home page

    METHODS:
        __init__(self, view, model, event_system)
        get_passwords_from_database(self)
        get_password_by_title(self, title)

    ATTRIBUTES:
        passwords: list - List of saved Password objects

    INTERFACE INFO:
        get_passwords_from_database() - Retrieves passwords from the database and updates the password list
        get_password_by_title() - Retrieves a password by title from the password
    '''
    def __init__(self):
        self.passwords = []

    def retrieve_passwords_from_database(self) -> bool:
        '''
        Retrieve passwords from the database and update local password list
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return bool
        '''
        #clear out current passwords and overwrite with passwords from database
        result = True
        self.passwords = []
        try:
            cxn = connect()
            cursor = cxn.cursor()
            query = "SELECT website_title, url, username, encrypted_pass, date_created FROM Passwords"
            cursor.execute(query)
            results = cursor.fetchall()

            for row in results:
                website_title = row[0]
                url = row[1]
                username = row[2]
                encrypted_pass = row[3]
                date_created = row[4]

                print(encrypted_pass)

                decryption = Decryption(encrypted_pass)
                decrypted_pass = decryption.apply_cipher()

                print(decrypted_pass)

                password = Password(website_title, url, username, decrypted_pass, date_created)
                self.passwords.append(password)

        except mysql.connector.Error as error:
            print(f"oopsie!", error)
            result = False
        finally:
            cursor.close()
            cxn.close()
        
        return result

    def get_passwords(self) -> list:
        return self.passwords

    def get_password_by_title(self, title: str) -> str:
        '''
        Retrieve passwords by title from the password list
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        result = None
        for password in self.passwords:
            if title == password.get_title():
                result = password
                break

        return result
