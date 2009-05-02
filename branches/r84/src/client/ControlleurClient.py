import xmlrpclib
import pickle
from threading import Timer

from modele import *
from Vue import Vue
from Messageur import Messageur

class Controlleur(object):
    def __init__(self):
        self.vue=Vue(self)
        self.nom = None
        self.couleur = None
        self.ip = None
        self.serveur = None
        self.univers = None
        self.player = None
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.vue.root.mainloop()
        self.tDeplacement.cancel()
            
    def ConnecterAuServeur(self):
        self.serveur = xmlrpclib.Server('http://localhost:8000')
        self.univers = pickle.loads(self.serveur.ConnecterJoueur(self.nom))
        self.player = self.univers.joueurs[self.nom]
        
        self.player.ajouterVaisseau(50,50)
        self.player.vaisseaux[0].nom = "premier"
        self.vue.zoneJeu.nouveauVaisseau(self.player.vaisseaux[0])
        
        self.messageADecoder = None
        
        self.chat = Messageur(self)
        self.vue.zoneJeu.initialiserSystemes(self.univers.systemes)
        self.selectione = "false" # a mettre dans les entite
        self.tDeplacement.start()
        
    def SelectionneEntite(self,event):
        #Selectionne une entite et dessine un rond autour
        #print "entite selectione"
        pass
    
    def Action(self, x, y):
        typeDeplacement = "deplacement"
        if typeDeplacement == "deplacement":     
            self.player.vaisseaux[0].xArrivee = x
            self.player.vaisseaux[0].yArrivee = y
        
    def RefreshDeplacement(self):
        # pour entrer danss cette fonction continuellement
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.tDeplacement.start()
        self.SendNewDeplacement()
        
        
    def SendNewDeplacement(self):
        self.player.vaisseaux[0].deplacer()
        self.vue.zoneJeu.deplacerVaisseau(self.player.vaisseaux[0])
        self.serveur.MiseAJourVaisseaux(self.nom, pickle.dumps(self.univers.joueurs[self.nom].vaisseaux))
        self.mes1 = self.serveur.requeteClient(self.nom)
        if self.mes1 == "rien":
            pass
        else:
            listeMessage = pickle.loads(self.serveur.requeteClient(self.nom))
            self.DecodeMessage(listeMessage)
    
    def RefreshVue(self,NomduJoueur):
        for i in self.univers.joueurs[NomduJoueur].vaisseaux:
            unVaisseau = self.vue.zoneJeu.nouveauVaisseau(self.univers.joueurs[NomduJoueur].vaisseaux[0])
            self.vue.zoneJeu.deplacerVaisseau(unVaisseau)
    
    def TypeAction(self,x,y):
        #"deplacement" pour test, cette fonction verifiera le type
        #a passer en parametre a self.action
        self.Action(x,y)
        
    def DecodeMessage(self,listeDesMessages): #nom type objet
        if len(listeDesMessages) > 0:           
            for i in listeDesMessages:
                messageADecoder = listeDesMessages.pop()
                if (messageADecoder[1] == "vai"):
                    self.univers.joueurs[messageADecoder[0]].vaisseaux = messageADecoder[2]
                    self.RefreshVue(messageADecoder[0])
            
        
        
            
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
        elif event.num == 2:
            self.player.ajouterVaisseau(event.x,event.y)
            

        
    def BoiteConnection(self,nomJoueur,ip,couleur=""):
        print "entre"
        self.nom = nomJoueur
        self.ip = ip
        self.couleur = "vert"
        self.vue.demarrerJeu()
        self.ConnecterAuServeur()
        
        

if __name__=="__main__":
    controlleur = Controlleur()
