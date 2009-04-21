#!/usr/bin/env python

#Ce client teste la communication avec le serveur.

import xmlrpclib
import cPickle as pickle

from modele import *


adresse_serveur = 'http://127.0.0.1:8000'
serveur = xmlrpclib.Server(adresse_serveur)

class Client(object):
    def __init__(self):


        #test des systemes
        self.testSystemes()
        #test de la fonction chat
        self.testChat()
        #test de la creation de joueur
        self.testJoueur()


    ########################
    #debut de la partie chat
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

    '''cette methode affiche um message.'''
    def returnMessage(self, noMsg):
        self.message = serveur.returnMessage(noMsg)

        #le serveur retourne un "tuple"; 0 contient le nom et 1 le message.
        print self.message[0] + ":" + self.message[1]


    #fin de la partie chat
    ########################
    #debut de la partie sync
    def syncClient(self):
        pass
    #fin de la partie sync
    ########################
    #debut de la partie test


    #cette methode teste le transfert de systemes client-serveur
    def testSystemes(self):
        self.orion = pickle.loads(serveur.pushSystemes().data)

        for x in range (self.orion.nbrSystemes):
            print "systeme id. ",
            print self.orion.systemes[x].id,
            print " x:",
            print self.orion.systemes[x].x ,
            print "y:",
            print self.orion.systemes[x].y


    #cette methode teste le chat
    def testChat(self):
        self.noMsg = 0
        #j'envoie des messages bidons
        serveur.addMessage("chryana","allo")
        serveur.addMessage("michel","byebye!")
        serveur.addMessage("benoit","salut")

        self.currentMessage()


    def testJoueur(self):
        print serveur.addJoueur("chryana")
        #test si accepte deux clients avec nom identique
        print serveur.addJoueur("chryana")

        self.orion.joueurs=pickle.loads(serveur.pushJoueurs().data)

        for x in self.orion.joueurs.keys():
            print "le vaisseau de ",
            print self.orion.joueurs[x].nick,
            print "est a la coordonnee (",
            print self.orion.joueurs[x].vaisseaux[0].x,
            print ",",
            print self.orion.joueurs[x].vaisseaux[0].y,
            print ")"




    #fin de la partie test
    ######################



    def getFriendlyShipData(self):
        serveur.getFriendlyShipData()



        


unclient = Client()

