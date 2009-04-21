#!/usr/bin/env python

#ce fichier test initialise un univers tres simple afin de tester le fonctonnement de la vue.

import sys

sys.path.append('../client:../modele')


from Univers import Univers
from Systeme import Systeme
from Vaisseau import Vaisseau

from affichage import *


class UniversTest:
    def __init__(self):
        lUnivers = Univers()

        planeteX=Systeme(3,4)
        planeteY=Systeme(9,10)

        lUnivers.ajouterSysteme(planeteX)
        lUnivers.ajouterSysteme(planeteY)

        #j'interagit entre le modele et la vue pour des raisons de test
        x=Dessin()
        x.refreshSystemes(lUnivers.systemes)


unUnivers=UniversTest()

