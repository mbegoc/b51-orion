#l'univers
from modele.Joueur import Joueur
from modele.Systeme import Systeme

import random

class Univers(object):
    def __init__(self):
        self.tailleX=500
        self.tailleY=600
        self.joueurs = {}
        
        self.couleursJoueurs=["blue","green","purple","orange","yellow","red"]    # Une couleur pour chaque joueur

        self.systemes=[]
        
#        self.nbrSystemes = 100 #nombre de systemes dans l'univers existant
#        self.systemes = range(self.nbrSystemes)#les systemes seront places dans cette variable
#        self.initUniverse()
#        
#    def initUniverse(self):
#        for x in range(self.nbrSystemes):#je vais changer ca pour un shuffle plus tard pour eviter les collisions             
#              self.systemes[x]=Systeme(random.randint(0,50)*10,random.randint(0,50)*10) 
        
    def ajouterJoueur(self,id):
        couleur=self.couleursJoueurs.pop()
        system=self.systemes.pop()
        self.joueurs[id]=Joueur(self,id,couleur,system)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)
        
    def validePositionSysteme(self,testX,testY):
        valRet=0
        for i in range(len(self.systemes)):
            if(testX==self.systemes[i].x and testY==self.systemes[i].y):
                valRet=1
        return valRet        

            
            
            
            
            
            
            
