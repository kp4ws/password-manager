class Password:
    '''
    Password blueprint for a password object to be stored and retrieved in the database
    METHODS:
        __init__(self, title, password)
        get_title(self)
        get_password(self)
        set_title(self, title)
        set_password(self, password)
        __str__(self)
    
    ATTRIBUTES:
        title: str - Title of the password
        password: str - Password of the password
    
    INTERFACE INFO:
        get_title() - Returns title
        get_password() - Returns password
        set_title() - Sets title
        set_password() - Sets password
    '''

    def __init__(self, title: str, password: str) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :arg title: Title to be assigned
        :arg password: Password to be assigned
        :except No exceptions thrown by this method
        :return None
        '''
        self.title = title
        self.password = password
    
    def get_title(self) -> str:
        '''
        Retrieve the password title
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.title
    
    def get_password(self) -> str:
        '''
        Retrieve the password password
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return str
        '''
        return self.password
    
    def set_title(self, title) -> None:
        '''
        Set the password title
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.title = title

    def set_password(self, password: str) -> None:
        '''
        Set the password password
        :arg self: Required by python
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