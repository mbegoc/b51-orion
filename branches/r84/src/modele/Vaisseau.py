class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = x
        self.yArrivee = y
        self.nom = "untest"
        
    def deplacer(self):
        if self.x < self.xArrivee:
            self.x = self.x+5
        elif self.x > self.xArrivee:
            self.x = self.x-5
            
        if self.y < self.yArrivee:
            self.y = self.y+5
        
        elif self.y > self.yArrivee:
            self.y = self.y-5
        
            
        