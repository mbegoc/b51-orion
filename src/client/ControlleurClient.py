import xmlrpclib
import cPickle as pickle
from threading import Timer

from modele import *
from Vue import Vue
from Messageur import Messageur

class Controlleur(object):
    def __init__(self):
        self.serveur = xmlrpclib.Server('http://localhost:8000')
        self.univers = pickle.loads(self.serveur.ConnecterJoueur("benoit"))
        self.player = self.univers.joueurs["benoit"]
        self.player.ajouterVaisseau(50,50)
        self.chat = Messageur(self)
        self.vue=Vue(self)
        self.selectione = "false" # a mettre dans les entite
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.tDeplacement.start()
        self.vue.root.mainloop()
        self.tDeplacement.cancel()
            
    def SelectionneEntite(self,event):
        #Selectionne une entite et dessine un rond autour
        #print "entite selectione"
        pass
    
    def Action(self,event,typeDeplacement):
        if typeDeplacement == "deplacement":     
            self.player.vaisseaux[0].xArrivee = event.x
            self.player.vaisseaux[0].yArrivee = event.y
            self.player.vaisseaux[0].deplacer
            self.vue.zoneJeu.deleteCroix()
            self.vue.zoneJeu.drawCroix(event)
        
    def RefreshDeplacement(self):
        # pour entrer danss cette fonction continuellement
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.tDeplacement.start()
        self.vue.zoneJeu.PrintVaisseau(50,50)
        self.SendNewDeplacement()
        
    def SendNewDeplacement(self):
        #print "send un deplacement"
        pass
    
    def TypeAction(self,event):
        #"deplacement" pour test, cette fonction verifiera le type
        #a passer en parametre a self.action
        self.Action(event,"deplacement")

        
    #gere les clicks de souris sur le canvas
    def ClickEvent(self,event):
        if event.num == 1:
            #add un autre if pour savoir si il y a quelque chose a selectionner
            if self.selectione == "false":  
                self.SelectionneEntite(event)
                #remplacer les event par le cadre de l'objet selectionne
                self.vue.zoneJeu.rondSelection = self.vue.zoneJeu.create_oval(event.x-10,event.y-15,event.x+15,event.y+15, outline="red",width=2) 
                self.selectione = "true"
            else:
                self.vue.zoneJeu.delete(self.vue.zoneJeu.rondSelection)
                self.selectione = "false"
            
            self.vue.zoneJeu.deleteCroix()
        elif event.num == 3:
            #pour savoir si il faut deplacer,attaquer,conquerir...
            self.TypeAction(event)

        
        

if __name__=="__main__":
    controlleur = Controlleur()
