from events import EventChannel
from views import HomeView
from models import HomeModel

class HomeController:
    '''
    Serves as the Controller for the HomeView and HomeModel

    METHODS:
        __init__(self, view, model, event_system)
        show_view(self)
        _subscribe(self)
        _bind(self)
        _handle_create(self)

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

    def _handle_create(self) -> None:
        '''
        Handles pressing the Create button in the HomeView
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.event_system.trigger(EventChannel.CREATE_PASSWORD_VIEW)