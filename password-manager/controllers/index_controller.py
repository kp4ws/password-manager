'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

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
        #self.view.button_enter.config(command=self._handle_enter)
        self.view.button_enter.bind("<Button-1>", self._handle_enter)
        self.view.canvas_game.bind("<KeyPress>", self._player_physics)

    def _handle_enter(self, event) -> None:
        '''
        Handles pressing the Enter button in the IndexView
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        if self.view.button_enter.cget("state") == "disabled":
            self.view.show_captcha_error()
            return
        
        self.event_system.trigger(EventChannel.HOME_VIEW)

    
    def _player_physics(self, event) -> None:
        if self.model.get_captcha_completed():
            return

        #Move Player
        player_x, player_y = 0, 0
        if event.keysym == "Up":
            player_y = -30
        elif event.keysym == "Down":
            player_y = 30
        elif event.keysym == "Left":
            player_x = -30
        elif event.keysym == "Right":
            player_x = 30

        self.view.canvas_game.move(self.view.player, player_x, player_y)


        #Check for collisions
        player_bbox = self.view.canvas_game.bbox(self.view.player)
        flag_bbox = self.view.canvas_game.bbox(self.view.red_flag)

        if player_bbox and flag_bbox:
            overlapping_items = self.view.canvas_game.find_overlapping(*player_bbox)

            # If collision with flag, captcha is completed
            if self.view.red_flag in overlapping_items:
                
                # Simulate changing red flag to green flag by moving red flag off screen
                self.view.canvas_game.move(self.view.red_flag, 1000, 1000) 

                self.view.label_captcha.config(text="CAPTCHA Completed", fg="green")
                self.view.button_enter.config(state="normal")
                self.model.set_captcha_completed(True)
