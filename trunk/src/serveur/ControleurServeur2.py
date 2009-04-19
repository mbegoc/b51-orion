from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

import xmlrpclib

import cPickle as pickle
#import datetime

import random
from modele import *




# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class ControleurServeur(object):
    def __init__(self):
        self.orion=Univers.Univers()
        
        #ce code affiche les coordonnees des systemes crees
        '''
        print "debug"
        for x in range (self.orion.nbrSystemes):
            print "systeme no. ",
            print x,
            print " x:",
            print self.orion.systemes[x].x ,
            print "y:",
            print self.orion.systemes[x].y
            '''

    def pushSystemes(self):
        return xmlrpclib.Binary(pickle.dumps(self.orion))


class Serveur(object):
    def __init__(self):
        self.server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler)
        self.controleur=ControleurServeur()

        #self.server.register_function(pushSystemes, 'pushSystemes')

        self.server.register_instance(self.controleur)

        # Demarrer la boucle du serveur
        try:
            print "serveur demarre"
            print 'Tapez Control-C pour sortir'
            self.server.serve_forever()
        except KeyboardInterrupt:
            print 'Termine!'
