class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = None
        self.yArrivee = None
        
    def deplacer(self, x, y):
        pass
    
