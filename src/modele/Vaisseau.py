class Vaisseau(object):
    def __init__(self, x, y, id="default", classe="civil", type="default"):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = x
        self.yArrivee = y
        self.id = id
        self.type = type
        self.classe = classe
        
    def deplacer(self):
        if self.x < self.xArrivee:
            self.x = self.x+1
        elif self.x > self.xArrivee:
            self.x = self.x-1
            
        if self.y < self.yArrivee:
            self.y = self.y+1
        
        elif self.y > self.yArrivee:
            self.y = self.y-1
        
            
        