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

        self.systemes={}
        
#        self.nbrSystemes = 100 #nombre de systemes dans l'univers existant
#        self.systemes = range(self.nbrSystemes)#les systemes seront places dans cette variable
#        self.initUniverse()
#        
#    def initUniverse(self):
#        for x in range(self.nbrSystemes):#je vais changer ca pour un shuffle plus tard pour eviter les collisions             
#              self.systemes[x]=Systeme(random.randint(0,50)*10,random.randint(0,50)*10) 
        
    def ajouterJoueur(self,id,arbre):
        print "here2"
        couleur=self.couleursJoueurs.pop()
        d=self.systemes
        ld=d.keys()
        print "herepopo"
        a=ld.pop()
        print self.systemes[a]
        print "outpopo"
        system=self.systemes[a]
        self.joueurs[id]=Joueur(self,id,couleur,system,arbre)
        print "here_3"
        
    def ajouterSysteme(self, systeme):
        self.systemes[systeme.id]=systeme
        
    def validePositionSysteme(self,testX,testY):
        valRet=0
        for i in self.systemes:
            if(testX==self.systemes[i].x and testY==self.systemes[i].y):
                valRet=1
        return valRet        

            
            
            
            
            
            
            
