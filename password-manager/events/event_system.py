class EventSystem:
    def __init__(self):
        self.subscriptions = {}

    def subscribe(self, event, callback):
        if event not in self.subscriptions:
            self.subscriptions[event] = []
        self.subscriptions[event].append(callback)
    
    def unsubscribe(self, event, callback):
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)
    
    def trigger(self, event, *args, **kwargs):
        if event in self.subscriptions:
            for callback in self.subscriptions[event]:
                callback(*args, **kwargs)