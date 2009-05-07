from modele.Ressources import Ressources
from modele.Evenements import *

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
        self.ressourcesPropulsion.gaz = 20
        
        self.ecouteurs = []
        
    def deplacer(self):
        self.ressourcesPropulsion.consommer(self.ressourcesEntretien)
        if self.x != self.xArrivee or self.y != self.yArrivee:
            if self.ressourcesPropulsion.gaz >= 0:
                if self.x < self.xArrivee:
                    self.x = self.x+5
                elif self.x > self.xArrivee:
                    self.x = self.x-5
                    
                if self.y < self.yArrivee:
                    self.y = self.y+5
                
                elif self.y > self.yArrivee:
                    self.y = self.y-5
            else:
                #on genere un evenement car le vaisseau n'a plus suffisamment de ressources pour se deplacer
                self.genererEvent("Panne", "Ressources insuffisantes pour se deplacer")

    ''' GESTION DES EVENEMENTS '''
    #ajout des ecouteurs sur l'objet
    def addVaisseauListener(self, ecouteur):
        self.ecouteurs.append(ecouteur)
    
    #enlever des ecouteurs
    def removeVaisseauListener(self, ecouteur):
        self.ecouteurs.remove(ecouteur)
    
    #generation d'un evenement: on cree l'objet evenment, et on le passe à la liste d'ecouteurs inscrits
    #pour s'inscrire, un ecouteur DOIT IMPERATIVEMENT POSSEDER UNE METHODE vaisseauEvent(event)
    def genererEvent(self, type, message, code=0):
        ve = VaisseauEvent(self, type, message, code)
        for ecouteur in self.ecouteurs:
            ecouteur.vaisseauEvent(ve)



'''    TEST    '''
#classe ecouteur de test         
class VaisseauEcouteur(object):
    def __init__(self):
        pass
    
    def vaisseauEvent(self, ve):
        print "le vaisseau est en panne a la position: ",
        print ve.source.x, ", ", ve.source.y

if __name__ == "__main__":
    vaisseau = Vaisseau(50, 50)
    vaisseau.xArrivee = 300

    ecouteur = VaisseauEcouteur()
    vaisseau.addVaisseauListener(ecouteur)
    
    for i in range(0,30):
        vaisseau.deplacer()