#!/usr/bin/env python

import math


class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.vitesse = 10.0

    #place dans une methode pour eviter de jouer avec les variables de l'objet
    def moveVaisseau(self, x, y):
        self.xArrivee = x
        self.yArrivee = y

        self.moveX = self.xArrivee - self.x
        self.moveY = self.yArrivee - self.y

        self.angle = math.atan2(self.moveY, self.moveX)

        self.vitesseY = self.vitesse * math.sin(self.angle)
        self.vitesseX = self.vitesse * math.cos(self.angle)


    #False indique au controleur que le deplacement est termine.
    def deplacement(self):
        #va devoir etre ameliore pour eviter les cas ou le vaisseau fait de tres
        #petits changements dans sa direction sur un axe donne
        if ((self.xArrivee - self.x) <= self.vitesseX) and ((self.yArrivee - self.y) <= self.vitesseY):
            self.x = self.xArrivee
            self.y = self.yArrivee
            return False
        else:
            self.x = self.x + self.vitesseX
            self.y = self.y + self.vitesseY
            return True

