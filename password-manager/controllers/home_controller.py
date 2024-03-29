from events import EventChannel
from views import HomeView
from models import HomeModel
from tkinter import END
from domain import Password

class HomeController:
    '''
    Serves as the Controller for the HomeView and HomeModel

    METHODS:
        __init__(self, view, model, event_system)
        show_view(self)
        _subscribe(self)
        _bind(self)
        _handle_create(self)
        _handle_password_select(self)
        _update_passwords(self)

    ATTRIBUTES:
        view: HomeView - View associated with this Controller
        model: HomeModel - Model associated with this Controller
        event_system: EventSystem - Event system of the application

    INTERFACE INFO:
        show_view() - Displays the view associated with this controller
    '''
    def __init__(self, view: HomeView, model: HomeModel, event_system) -> None:
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
        self._update_passwords()
        self.view.tkraise()

    def _subscribe(self) -> None:
        '''
        Subscribes event callbacks for this Controller
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.event_system.subscribe(event=EventChannel.HOME_VIEW, callback=self.show_view)

    def _bind(self) -> None:
        '''
        Binds commands from the associated View
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.view.button_create.config(command=self._handle_create)
        self.view.button_modify.config(command=self._handle_modify)
        self.view.listbox_saved_passwords.bind("<<ListboxSelect>>", self._handle_password_select)

    def _handle_create(self) -> None:
        '''
        Handles pressing the Create button in the HomeView
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.event_system.trigger(EventChannel.CREATE_PASSWORD_VIEW)
    
    def _handle_modify(self) -> None:
        '''
        Handles pressing the Modify button in the HomeView
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        selection = self.view.listbox_saved_passwords.curselection()
        if not selection:
            self.view.show_modify_error()
            return

        index = selection[0]
        selected_item = self.view.listbox_saved_passwords.get(index)
        self.event_system.trigger(EventChannel.MODIFY_PASSWORD_VIEW, selected_item)

    def _handle_password_select(self, event) -> None:
        '''
        Handles selecting a password from the saved passwords list
        :arg self: Required by python
        :arg event: Event associated with the password selection
        :except No exceptions thrown by this method
        :return None
        '''
        selection = self.view.listbox_saved_passwords.curselection()
        if selection:
            index = selection[0]
            selected_item = self.view.listbox_saved_passwords.get(index)
            
            password = self.model.get_password_by_title(selected_item)

            # Update the password details
            self.view.label_selected_title.config(text=f'Title: {password.get_title()}')
            self.view.label_selected_url.config(text=f'URL: {password.get_url()}')
            self.view.label_selected_username.config(text=f'Username: {password.get_username()}')
            self.view.label_selected_password.config(text=f'Password: {password.get_password()}')
            self.view.label_selected_date.config(text=f'Date Created: {password.get_created_date()}')


    def _update_passwords(self) -> None:
        '''
        Populates passwords into the saved passwords list
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        password_flag = self.model.retrieve_passwords_from_database()

        if not password_flag:
            self.view.show_error_retrieving_passwords()
            return
        
        passwords = self.model.get_passwords()
        self.view.listbox_saved_passwords.delete(0, END)
        for password in passwords:
            self.view.listbox_saved_passwords.insert(END, password)