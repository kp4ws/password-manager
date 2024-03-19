from events import EventChannel
from views import CreatePasswordView
from models import CreatePasswordModel

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
        self.view.button_back.config(command=self._handle_back)
    
    def _handle_back(self):
        self.event_system.trigger(EventChannel.HOME_VIEW)
    
    def _handle_submit(self):
        data = {}
        pass