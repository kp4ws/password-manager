from events import EventChannel

class HomeController:
    def __init__(self, view, model, event_system):
        self.view = view
        self.model = model
        self.event_system = event_system
        self.subscribe()
        self.bind()

    def show_view(self):
        self.view.tkraise()

    def subscribe(self):
        self.event_system.subscribe(event=EventChannel.HOME_VIEW, callback=self.show_view)

    def bind(self):
        self.view.button_create.config(command=self._handle_create)

    def _handle_create(self):
        self.event_system.trigger(EventChannel.CREATE_PASSWORD_VIEW)