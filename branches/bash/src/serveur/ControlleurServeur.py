from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import pickle
import datetime
import random
from modele.Systeme import Systeme
from modele.Univers import Univers
from modele.Joueur import Joueur

# Creer un serveur
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=SimpleXMLRPCRequestHandler)


# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class ControleurServeur(object):
    def __init__(self):
        self.idJoueur=0
    def ConnecterJoueur(self):
        if(len(Univers.joueurs)==0):
           for s in range(1,10):             
              Systeme.x=random.randint(0,50)*10 
              Systeme.y=random.randint(0,60)*10
              if(Univers.systemes.count(Systeme)):
                s=s-1
              else:               
                Univers.ajouterSysteme(Systeme)
             
    def AjouterSysteme(self,x,y):
        Systeme.x=x
        Systeme.y=y
        pass



server.register_instance(ControleurServeur())

# Demarrer la boucle du serveur
print "OK, serveur demarre"
server.serve_forever()
print "OK, serveur arrete"
