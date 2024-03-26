from events import EventChannel
from views import CreatePasswordView
from models import CreatePasswordModel
from datetime import datetime
from domain import Password

class CreatePasswordController:
    '''
    Serves as the Controller for the CreatePasswordView and CreatePasswordModel

    METHODS:
        __init__(self, view, model, event_system)
        show_view(self)
        _subscribe(self)
        _bind(self)

    ATTRIBUTES:
        view: CreatePasswordView - View associated with this Controller
        model: CreatePasswordModel - Model associated with this Controller
        event_system: EventSystem - Event system of the application

    INTERFACE INFO:
        show_view() - Displays the view associated with this controller
    '''
    def __init__(self, view: CreatePasswordView, model: CreatePasswordView, event_system) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :arg view: View associated with this Controller
        :arg model: Model associated with this Controller
        :arg event_system: Event system of the application
        :except No exceptions thrown by this method
        :return None
        '''
        self.view = view
        self.model = model
        self.event_system = event_system
        self._subscribe()
        self._bind()

    def show_view(self) -> None:
        '''
        Displays the View for this Controller
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.view.tkraise()

    def _subscribe(self) -> None:
        '''
        Subscribes event callbacks for this Controller
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.event_system.subscribe(event=EventChannel.CREATE_PASSWORD_VIEW, callback=self.show_view)

    def _bind(self) -> None:
        '''
        Binds commands from the associated View
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.view.button_clear.config(command=self._handle_clear)
        self.view.button_back.config(command=self._handle_back)
        self.view.button_submit.config(command=self._handle_submit)
    
    def _handle_clear(self):
        self.view.var_title.set("")
        self.view.var_url.set("")
        self.view.var_username.set("")
        self.view.var_password.set("")

    def _handle_back(self):
        self._handle_clear()
        self.event_system.trigger(EventChannel.HOME_VIEW)
    
    def _validate_password(self, title, url, username, password) -> bool:
        if title == "" or username == "" or password == "":
            self.view.show_general_error()
            return False
        
        if len(password) < 8 or len(password) > 16:
            self.view.show_password_length_error()
            return False
        
        return True

    def _handle_submit(self):
        title = self.view.var_title.get()
        url = self.view.var_url.get()
        username = self.view.var_username.get()
        _password = self.view.var_password.get()
        current_date = datetime.now().date()

        password_flag = self._validate_password(title, url, username, _password)

        if not password_flag:
            return

        password = Password(title, url, username, _password, current_date)
        save_flag = self.model._save_password_to_database(password)

        if not save_flag:
            self.view.show_error_saving_password()
            return
        
        self.view.show_success()
        self._handle_clear()
        self.event_system.trigger(EventChannel.HOME_VIEW)

