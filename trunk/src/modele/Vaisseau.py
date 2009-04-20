class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = x
        self.yArrivee = y
        
    def deplacer(self): # 10 est un nombre test
        if self.x < self.xArrivee:
            self.x = self.x+10
        elif self.x > self.xArrivee:
            self.x = self.x+10     
        if self.y < self.yArrivee:
            self.y = self.y+10
        elif self.y > self.yArrivee:
            self.y = self.y+10
        

    
