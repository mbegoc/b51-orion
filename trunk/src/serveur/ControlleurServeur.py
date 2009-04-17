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
class ControlleurServeur(object):
    def __init__(self):
        self.univers = Univers
    def ConnecterJoueur(self, nom):
        if(not self.univers.joueurs):
           for s in range(1,10):             
              Systeme.x=random.randint(0,50)*10 
              Systeme.y=random.randint(0,60)*10
              if(self.univers.systemes.count(Systeme)):
                s=s-1
              else:               
                self.univers.ajouterSysteme(Systeme)
        self.univers.ajouterJoueur(nom)
        
    def MiseAJourVaisseaux(self,nom,messVaisseaux):
        self.univers.joueurs[nom].vaisseaux=pickle.loads(messVaisseaux)
        MisaJourMessage(nom,"vai", self.univers.joueurs[nom].vaisseaux)

    
             
    def MiseAJourMessage(self, nom, codMess, messObj):
        for s in self.univers.joueurs:
            if(self.univers.joueurs[s].id <> nom):
                self.univers.joueurs[s].message.append(nom, codMess, messObj)
                
    def requeteClient(self, nom):
        if(self.univers.joueurs[nom].message):
            return pickle.dumps(self.univers.joueurs[nom].message) 



server.register_instance(ControlleurServeur())

# Demarrer la boucle du serveur
print "OK, serveur demarrer"
server.serve_forever()
print "OK, serveur arreter"
