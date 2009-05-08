from modele.Ressources import Ressources
from modele.Evenements import *

import math


class Vaisseau(object):
    def __init__(self,parent, x, y, id="default", classe="civil", type="default"):
        self.parent=parent
        self.x = x
        self.y = y
        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple
        self.xArrivee = x
        self.yArrivee = y
        self.vitesse = 5
        self.idDestination=0 # pour met id dictionaire du systeme s'il n'y pas de systeme valeur=0
        
        self.id = id
        self.type = type
        self.classe = classe
        self.ressourcesEntretien = Ressources(0)
        self.ressourcesEntretien.gaz = 0
        
        self.ressourcesPropulsion = Ressources(0)
        self.ressourcesPropulsion.gaz = 20
        
        self.ecouteurs = []
    def valideArriveSysteme(self): # valide que le vaisseau arribe à un systeme
        if self.x==self.xArrivee and self.y==self.yArrivee and Univers.systemes[self.idDestination]:
            return true
        else:
            return false 
        
    def deplacer(self):
        self.ressourcesPropulsion.consommer(self.ressourcesEntretien)
        if self.x != self.xArrivee or self.y != self.yArrivee:
            if self.ressourcesPropulsion.gaz >= 0:
                if self.xArrivee - self.x == 0:
                    if self.yArrivee - self.y < 0:
                        direction = -math.pi/2
                    else:
                        direction = math.pi/2
                else:
                    direction = math.atan((self.yArrivee - self.y)/(self.xArrivee - self.x))
                    if self.xArrivee - self.x < 0:
                        if direction > 0:
                            direction = -math.pi + direction
                        else:
                            direction = math.pi + direction

                #ensuite on calcule la nouvelle position
                newX = self.vitesse * math.cos(direction)
                newY = self.vitesse * math.sin(direction)

                #on verifie si on est arrive a destination
                #si oui, on place le vaisseau a la position d'arrivee (pour eviter de la depasser)
                #sinon on place le vaisseau a la nouvelle position
                xActuel = self.x
                self.x = self.x + int(newX)
                if self.xArrivee != xActuel:
                    if (self.xArrivee - xActuel)/math.fabs(self.xArrivee - xActuel) == 1:
                        if self.x > self.xArrivee:
                            self.x = self.xArrivee
                    elif (self.xArrivee - xActuel)/math.fabs(self.xArrivee - xActuel) == -1:
                        if self.x < self.xArrivee:
                            self.x = self.xArrivee

                yActuel = self.y
                self.y = self.y + int(newY)
                if self.yArrivee != yActuel:
                    if (self.yArrivee - yActuel)/math.fabs(self.yArrivee - yActuel) == 1:
                        if self.y > self.yArrivee:
                            self.y = self.yArrivee
                    elif (self.yArrivee - yActuel)/math.fabs(self.yArrivee - yActuel) == -1:
                        if self.y < self.yArrivee:
                            self.y = self.yArrivee

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
    
    #generation d'un evenement: on cree l'objet evenment, et on le passe a la liste d'ecouteurs inscrits
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