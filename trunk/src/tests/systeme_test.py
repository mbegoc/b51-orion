#!/usr/bin/env python

#ce fichier test initialise un univers tres simple afin de tester le fonctonnement de la vue.

from modele.Univers import Univers
from modele.Systeme import Systeme
from modele.Vaisseau import Vaisseau

class UniversTest:
    def __init__(self):
        lUnivers = Univers()

        planeteX=Systeme(3,4)
        planeteY=Systeme(9,10)

        lUnivers.ajouterSysteme(planeteX)
        lUnivers.ajouterSysteme(planeteY)

        #j'interagit entre le modele et la vue pour des raisons de test



