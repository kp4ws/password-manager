'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

class Password:
    '''
    Password blueprint for a password object to be stored and retrieved in the database
    METHODS:
        __init__(self, title, url, username, password, created_date)
        get_title(self)
        get_url(self)
        get_username(self)
        get_password(self)
        get_created_date(self)
        set_title(self, title)
        set_url(self, url)
        set_username(self, username)
        set_password(self, password)
        set_created_date(self, created_date)
        __str__(self)
    
    ATTRIBUTES:
        title: str - Title of the password
        url: str - URL of the password
        username: str - Username of the password
        password: str - Password of the password
        created_date: str - Creation date of the password

    INTERFACE INFO:
        get_title() - Returns title
        get_url() - Returns url
        get_username() - Returns username
        get_password() - Returns password
        get_created_date() - Returns created date
        set_title() - Sets title
        set_url() - Sets url
        set_username() - Sets username
        set_password() - Sets password
        set_created_date() - Sets created date
    '''

    def __init__(self, title: str, url: str, username: str, password: str, created_date: str) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :arg title: Title to be assigned
        :arg url: Url to be assigned
        :arg username: Username to be assigned
        :arg password: Password to be assigned
        :arg created_date: Created date to be assigned
        :except No exceptions thrown by this method
        :return None
        '''
        self.title = title
        self.url = url
        self.username = username
        self.password = password
        self.created_date = created_date
    
    def get_title(self) -> str:
        '''
        Retrieve the password's title
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.title
    
    def get_url(self) -> str:
        '''
        Retrieve the password's url
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.url

    def get_username(self) -> str:
        '''
        Retrieve the password's username
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.username

    def get_password(self) -> str:
        '''
        Retrieve the password's password
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.password
    
    def get_created_date(self) -> str:
        '''
        Retrieve the password's created date
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.created_date
    
    def set_title(self, title: str) -> None:
        '''
        Set the password title
        :arg self: Required by python
        :arg title: Title to be set
        :except No exceptions thrown by this method
        :return None
        '''
        self.title = title

    def set_url(self, url: str) -> None:
        '''
        Set the url
        :arg self: Required by python
        :arg url: Url to be set
        :except No exceptions thrown by this method
        :return None
        '''
        self.url = url

    def set_username(self, username: str) -> None:
        '''
        Set the username
        :arg self: Required by python
        :arg username: Url to be set
        :except No exceptions thrown by this method
        :return None
        '''
        self.username = username

    def set_created_date(self, created_date: str) -> None:
        '''
        Set the created date
        :arg self: Required by python
        :arg created_date: Created date to be set
        :except No exceptions thrown by this method
        :return None
        '''
        self.created_date = created_date

    def set_password(self, password: str) -> None:
        '''
        Set the password password
        :arg self: Required by python
        :arg password: Password to be set
        :except No exceptions thrown by this method
        :return None
        '''
        self.password = password

    def __str__(self) -> str:
        '''
        Overriden method used to modify the printed value of this object
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.title