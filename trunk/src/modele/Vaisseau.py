#!/usr/bin/env python

class Vaisseau(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.etat = "rien" # pour s'avoir s'il attaque ou s'il est mort par exemple

    #place dans une methode pour eviter de jouer avec les variables de l'objet
    def moveVaisseau(self, x, y):
        self.xArrivee = x
        self.yArrivee = y


    #a changer pour que le deplacement soit a la meme vitesse dans toutes les directions
    def deplacement(self):
        if self.x < self.xArrivee:
            self.x = self.x+10
        elif self.x > self.xArrivee:
            self.x = self.x+10     
        if self.y < self.yArrivee:
            self.y = self.y+10
        elif self.y > self.yArrivee:
            self.y = self.y+10
        

    
