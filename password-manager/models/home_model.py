from domain import Password
from encryption import Encryption
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

    def get_passwords_from_database(self) -> list:
        '''
        Retrieve passwords from the database and update local password list
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return list
        '''
        #TODO: retrieve passwords from the database

        self.query = 'select encrypted_pass from passwords select title from websites'

        while(rs.next()):
            Password(rs.getString(1), rs.getString(2)..... encrypt(rs.String(3)))
            self.passwords.append(Password)

        #Password("Password 1", "", "", "dfadfdsfasdf", ""),

        #decrypt password

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
