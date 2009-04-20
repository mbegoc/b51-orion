#!/usr/bin/env python

#Ce client teste la communication avec le serveur.

import xmlrpclib
import cPickle as pickle

from modele import *


adresse_serveur = 'http://127.0.0.1:8000'
serveur = xmlrpclib.Server(adresse_serveur)

class Client(object):
    def __init__(self):
        self.orion = pickle.loads(serveur.pushSystemes().data)
        
        #cette oartie teste l'envoie des systemes
        for x in range (self.orion.nbrSystemes):
            print "systeme no. ",
            print x,
            print " x:",
            print self.orion.systemes[x].x ,
            print "y:",
            print self.orion.systemes[x].y

    #cette methode teste le chat
    def testChat(self):
        self.noMsg = 0
        #j'emvoie des messages bidons
        serveur.addMessage("chryana","allo")
        serveur.addMessage("michel","byebye!")
        serveur.addMessage("benoit","salut")

        self.currentMessage()


    '''
    cette methode retourne le numero du dernier message du serveur
    si ce nombre est superieur au numero actuel du message imprime,
    le client demande les messages restants.
    '''
    def currentMessage(self):
        self.pending = serveur.currentMessage()
        for x in range(self.noMsg, self.pending):
            self.returnMessage(x)
        self.noMsg = self.pending

    #affiche um message.
    def returnMessage(self, noMsg):
        self.message = serveur.returnMessage(noMsg)
        print self.message[0] + ":" + self.message[1]
            
        
        


unclient = Client()
unclient.testChat()
