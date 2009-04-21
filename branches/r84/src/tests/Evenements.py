'''
Created on 2009-04-02

@author: Michel

C'est un test d'implantation d'evenement qui pourrait servir dans notre modele.
Ce qui est interessant avec ce systeme a mon avis, c'est que ca aide a decoupler
encore plus les objets les uns des autres. On n'a plus besoin de connaitre 
la methode a appeler, avec ses parametres, a quel moment l'appeler, etc. Il 
suffit juste de s'inscrire comme ecouteur sur l'objet, et lorsque l'evenement
intervient, un objet evenement contenant toutes les donnees necessaire est 
envoye aux listeners
'''
from threading import Timer

#notre evenement de systeme, c'est essentiellement un conteneur de donnees utiles
class SystemeEvent(object):
    def __init__(self, origine, nom, message, code):
        self.origine = origine
        self.nom = nom
        self.message = message
        self.code = code

'''les veritables classes de notre modele'''
#un systeme
class Systeme(object):
    def __init__(self, nom, dureeVie = 5.0):
        self.ecouteurs = []#un systeme pour etre ecoute par un ou plusieurs ecouteurs
        self.etat = "systeme"
        self.nom = nom
        self.t = Timer(dureeVie, self.detruire)#compte le temps de vie du systeme: pour les besoins de l'exemple
        self.t.start()
    
    #methode appelee par le compteur lorsque le systeme explose
    def detruire(self):
        self.etat = "supernovae"
        #creation de l'evenement qui sera envoye a tous les ecouteurs
        se = SystemeEvent(self, "explosion", "ce systeme est detruit", 1)
        for ecouteur in self.ecouteurs:
            print self.nom + " explose !"
            ecouteur.systemeEvent(se)
    
    #on a besoin de pouvoir ajouter des ecouteur: ils sont ajoutes dans une liste
    def addSystemeListener(self, ecouteur):
        self.ecouteurs.append(ecouteur)

#une civilisation
class Civilisation(object):
    def __init__(self):
        self.systemes = []#une civilisation peut s'implanter sur plusieurs systemes
        self.existe = 1#elle peut etre detruite, il faut savoir si elle existe ou non
    
    #attribution d'un systeme a la civilisation
    def attribuerSysteme(self, systeme):
        self.systemes.append(systeme)
        #lorsque la civilisation s'implante sur le systeme, elle commence a ecouter le systeme
        #afin d'etre informee des changements qui peuvent intervenir
        systeme.addSystemeListener(self)
    
    #c'est la methode qui sera appelee par le systeme quand un evenement interviendra
    def systemeEvent(self, se):
        #le systeme n'existe plus, il faut le retirer de notre liste et si c'etait
        #le dernier, notre civilisation disparait
        self.systemes.remove(se.origine)
        if(len(self.systemes)) == 0:
            self.existe = 0
    
if __name__ == "__main__":
    #creation de l'univers, notre systeme est cree
    systeme1 = Systeme("Soleil")
    systeme2 = Systeme("Etoile lointaine 1", 10.0)
    systeme3 = Systeme("Etoile lointaine 2", 7.0)
    print "L'univers emerge du neant"
    #deux civilisations emergent dans l'univers
    civilisation1 = Civilisation()
    civilisation1.attribuerSysteme(systeme1)
    print "Une civilisation emerge sur le systeme1"
    
    civilisation2 = Civilisation()
    civilisation2.attribuerSysteme(systeme2)
    print "Une autre civilisation colonise le systeme2"
    
    civilisation1.attribuerSysteme(systeme3)
    print "La premiere civilisation colonise un nouveau systeme"
    
    while civilisation1.existe == 1 or civilisation2.existe == 1:
        pass
    
    print "Toutes les civilisations ont disparu suite a la destruction de tous les systemes habites de l'univers"
