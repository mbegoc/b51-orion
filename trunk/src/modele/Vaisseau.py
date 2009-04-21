class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = x
        self.yArrivee = y
        self.vitesse = 5
        
    def deplacer(self): # 10 est un nombre test
        #while (self.x <> self.xArrivee or self.y <> self.yArrivee ):
            if self.x < self.xArrivee:
                self.x = self.x+self.vitesse
            elif self.x > self.xArrivee:
                self.x = self.x-self.vitesse 
 
            if self.y < self.yArrivee:
                self.y = self.y+self.vitesse
            elif self.y > self.yArrivee:
                self.y = self.y-self.vitesse

        
            
            
        

    
