from modele.Ressources import Ressources

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
        self.ressourcesEntretien = Ressources(0)
        self.ressourcesEntretien.gaz = 1
        self.ressourcesPropulsion = Ressources(0)
        self.ressourcesPropulsion.gaz = 5
        
    def deplacer(self):
        self.ressourcesPropulsion.consommer(self.ressourcesEntretien)
        if self.ressourcesPropulsion.gaz >= 0:
            if self.x < self.xArrivee:
                self.x = self.x+5
            elif self.x > self.xArrivee:
                self.x = self.x-5
                
            if self.y < self.yArrivee:
                self.y = self.y+5
            
            elif self.y > self.yArrivee:
                self.y = self.y-5
        
            
        