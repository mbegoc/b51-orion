#l'univers
from modele.Joueur import Joueur
from modele.Systeme import Systeme

import random

class Univers(object):
    def __init__(self):
        self.tailleX=500
        self.tailleY=600
        #self.joueurs = {}
        #self.x = {}

        #self.couleursJoueurs=["blue","green","purple","orange","yellow","red"]    # Une couleur pour chaque joueur
        
        self.nbrSystemes = 100 #nombre de systemes dans l'univers existant
        self.systemes = range(self.nbrSystemes)#les systemes seront places dans cette variable
        self.initUniverse()
        

    def initUniverse(self):#fonction sans repetition
        self.tailleU = self.tailleX * self.tailleY
        self.positions = random.sample(range(self.tailleU), self.nbrSystemes)
        for a in range(self.nbrSystemes):
            self.x=self.positions[a]%self.tailleX
            self.y=self.positions[a]/self.tailleX

            self.systemes[a]=Systeme(self.x,self.y)
        
    '''
    def ajouterJoueur(self,id):
        couleur=self.couleursJoueurs.pop()
        system=self.systemes.pop()
        self.joueurs[id] = Joueur(self,id,couleur,system)
        
    def tabarnakTest(self,id):
        self.x[id] = "1"
        print self.x
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)
        '''
