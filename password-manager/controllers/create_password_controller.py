from events import EventChannel

class CreatePasswordController:
    def __init__(self, view, model, event_system):
        self.view = view
        self.model = model
        self.event_system = event_system
        self.subscribe()
        self.bind()

    def show_view(self):
        self.view.tkraise()

    def subscribe(self):
        self.event_system.subscribe(EventChannel.CREATE_PASSWORD_VIEW, self.show_view)

    def bind(self):
        pass