from events import EventChannel

class IndexController:
    def __init__(self, view, model, event_system):
        self.view = view
        self.model = model
        self.event_system = event_system
        self.subscribe()
        self.bind()

    def show_view(self):
        self.view.tkraise()

    def subscribe(self):
        self.event_system.subscribe(event=EventChannel.INDEX_VIEW, callback=self.show_view)

    def bind(self):
        self.view.button_enter.config(command=self._handle_enter)

    def _handle_enter(self):
        self.event_system.trigger(EventChannel.HOME_VIEW)
