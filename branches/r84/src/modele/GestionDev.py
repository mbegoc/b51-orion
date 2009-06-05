class GestionDev(object):
    def __init__(self, parent):
        self.parent = parent
        self.total = 100
        self.dev = {"agriculture" : 0, "connaissance" : 0, "production" : 0, "militaire" : 0, "economie" : 0}