class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = None
        self.yArrivee = None
        
    def deplacer(self, x, y):
        if self.x < self.xArrivee:
            self.x = self.x+5
        elif self.x > self.xArrivee:
            self.x = self.x-5
            
        if self.y < self.yArrivee:
            self.y = self.y+5
        
        elif self.y > self.yArrivee:
            self.y = self.y-5
            
        if self.x > self.xArrivee or self.x < self.xArrivee:
            self.x = self.xArrivee
            
        if self.y > self.yArrivee or self.y < self.yArrivee:
            self.y = self.yArrivee
            
        
            
        