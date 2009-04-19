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
        
        #debug
        for x in range (self.orion.nbrSystemes):
            print "systeme no. ",
            print x,
            print " x:",
            print self.orion.systemes[x].x ,
            print "y:",
            print self.orion.systemes[x].y



unclient = Client()
