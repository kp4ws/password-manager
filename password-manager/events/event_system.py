'''
Primary Author: Kent Pawson
Contributor(s): N/A
'''

class EventSystem:
    '''
    Main event system of the application
    
    METHODS:
        __init__(self)
        subscribe(self, event, callback)
        unsubscribe(self, event, callback)
        trigger(self, event, *args, **kwargs)

    ATTRIBUTES:
        subscriptions: dict - Dictionary containing all subscriptions
    
    INTERFACE INFO:
        subscribe() - Register a callback function to be called when a given event is triggered
        unsubscribe() - Unregister a subscription
        trigger() - Invoke an event

    '''

    def __init__(self) -> None:
        '''
        Initializes the object
        :arg self: Required by python
        :except No exceptions thrown by this method
        :return None
        '''
        self.subscriptions = {}

    def subscribe(self, event, callback) -> None:
        '''
        Add a subscription to the subscriptions dictionary
        :arg self: Required by python
        :arg event: Event to subscribe to
        :arg callback: Callback method to be called for the given event
        :except No exceptions thrown by this method
        :return None
        '''
        if event not in self.subscriptions:
            self.subscriptions[event] = []
        self.subscriptions[event].append(callback)
    
    def unsubscribe(self, event, callback) -> None:
        '''
        Remove a subscription to the subscriptions dictionary
        :arg self: Required by python
        :arg event: Event to unsubscribe from
        :arg callback: Callback method to be unsubscribed from
        :except No exceptions thrown by this method
        :return None
        '''
        if event in self.subscribers and callback in self.subscribers[event]:
            self.subscribers[event].remove(callback)
    
    def trigger(self, event, *args, **kwargs) -> None:
        '''
        Trigger an event
        :arg self: Required by python
        :arg event: Event to be triggered
        :arg *args: Positional arguments associated with the event
        :arg **kwargs: Keyword arguments associated with the event
        :except No exceptions thrown by this method
        :return None
        '''
        if event in self.subscriptions:
            for callback in self.subscriptions[event]:
                callback(*args, **kwargs)