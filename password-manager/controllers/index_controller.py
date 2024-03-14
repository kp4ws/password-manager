from events import EventSystem, EventChannel
from views import IndexView
from models import IndexModel

class IndexController:
    '''
    Serves as the Controller for the IndexView and IndexModel

    METHODS:
        __init__(self, view, model, event_system)
        show_view(self)
        _subscribe(self)
        _bind(self)
        _handle_enter(self)

    ATTRIBUTES:
        view: IndexView - View associated with this Controller
        model: IndexModel - Model associated with this Controller
        event_system: EventSystem - Event system of the application

    INTERFACE INFO:
        show_view() - Displays the view associated with this controller
    '''

    def __init__(self, view: IndexView, model: IndexModel, event_system: EventSystem) -> None:
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
        self.event_system.subscribe(event=EventChannel.INDEX_VIEW, callback=self.show_view)

    def _bind(self) -> None:
        '''
        Binds commands from the associated View
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.view.button_enter.config(command=self._handle_enter)

    def _handle_enter(self) -> None:
        '''
        Handles pressing the Enter button in the IndexView
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.event_system.trigger(EventChannel.HOME_VIEW)
