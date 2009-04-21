class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vitesse = 5.0

        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple


    #place dans une methode pour eviter de jouer avec les variables de l'objet
    def moveVaisseau(self, x, y):
        self.xArrivee = x
        self.yArrivee = y

        self.moveX = self.xArrivee - self.x
        self.moveY = self.yArrivee - self.y

        self.angle = math.atan2(self.moveY, self.moveX)

        self.vitesseY = self.vitesse * math.sin(self.angle)
        self.vitesseX = self.vitesse * math.cos(self.angle)


        
    def deplacer(self): 
        #while (self.x <> self.xArrivee or self.y <> self.yArrivee ):
            if self.x < self.xArrivee:
                self.x = self.x+self.vitesse
            elif self.x > self.xArrivee:
                self.x = self.x-self.vitesse 
 
            if self.y < self.yArrivee:
                self.y = self.y+self.vitesse
            elif self.y > self.yArrivee:
                self.y = self.y-self.vitesse

        
    #false indique au controleur que le deplacement est termine.
    def deplacement(self):
        #eventuellement je vais remplacer par arret apres avoir parcouru la distance requise.
        if ((self.xArrivee - self.x) <= self.vitesseX) and ((self.yArrivee - self.y) <= self.vitesseY):
            self.x = self.xArrivee
            self.y = self.yArrivee
            return False
        else:
            self.x = self.x + self.vitesseX
            self.y = self.y + self.vitesseY
            return True
            
            
        

    
