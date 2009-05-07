class Event(object):
    def __init__(self, source, type, message, code = 0):
        self.source = source
        self.type = type
        self.message = message
        self.code = code
    
class VaisseauEvent(Event):
    def __init__(self, source, type, message, code = 0):
        Event.__init__(self, source, type, message, code)
        
class RessourcesEvent(Event):
    def __init__(self, source, type, message, code = 0):
        Event.__init__(self, source, type, message, code)