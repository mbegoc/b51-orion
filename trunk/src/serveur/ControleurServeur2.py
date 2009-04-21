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
        self.chat=Chat.Chat()

        
    #envoie les systemes au joueur
    def pushSystemes(self):
        return xmlrpclib.Binary(pickle.dumps(self.orion))

    ############################
    #chat

    #ajoute un message au chat
    def addMessage(self, nick, message):
        self.chat.addMessage(nick, message)
        return 0 #une reponse est requise par le protocole

    '''
    renvoie le numero du dernier message sur le serveur.
    je suggere que cette fonction soit utilisee des qu'un client se connecte pour
    eviter que le client recoive tous les messages deja envoyes au serveur.
    '''
    def currentMessage(self):
        return self.chat.currentMessage()

    def returnMessage(self, numeroMsg):
        return self.chat.returnMessage(numeroMsg)

    #chat
    ##############
    #joueurs

    #ajoute un nouveau joueur
    def addJoueur(self, nick):
        if nick in self.orion.joueurs:
            return ("Ce nom existe deja")
        else:
            self.orion.addJoueur(nick)
            return ("ok")

    #renvoie tous les joueurs au client
    def pushJoueurs(self):
        return xmlrpclib.Binary(pickle.dumps(self.orion.joueurs))
    #joueurs
    ##############
    #vaisseaux

    def moveVaisseau(self, nick, noVaisseau):
        pass
    ##############
    #fermer le serveur

    def terminer(self):
        self.chat.terminer()




class Serveur(object):
    def __init__(self):
        self.server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=SimpleXMLRPCRequestHandler)
        self.controleur=ControleurServeur()

        self.server.register_instance(self.controleur)

        # Demarrer la boucle du serveur
        try:
            print "serveur demarre"
            print 'Tapez Control-C pour sortir'
            self.server.serve_forever()
        except KeyboardInterrupt:
            self.controleur.terminer()
            print 'Termine!'
