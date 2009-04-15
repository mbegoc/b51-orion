from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

#import pickle
#import datetime

import random
from modele import *




# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class ControleurServeur(object):
    def __init__(self):
        self.orion=Univers.Univers()
        
        #ce code affiche les coordonnees des systemes crees
        print "debug"
        for x in range (self.orion.nbrSystemes):
            print "systeme no. ",
            print x,
            print " x:",
            print self.orion.systemes[x].x ,
            print "y:",
            print self.orion.systemes[x].y

    '''
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
    '''

class Serveur(object):
    def __init__(self):
        self.server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler)
        self.controleur=ControleurServeur()
        self.server.register_instance(self.controleur)

        # Demarrer la boucle du serveur
        print "OK, serveur demarre"
        self.server.serve_forever()
        print "OK, serveur arrete"

