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
        self.ObjetSelectionne = None
        self.messageADecoder = None
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.vue.root.mainloop()
        self.tDeplacement.cancel()
            
    def ConnecterAuServeur(self):
        self.serveur = xmlrpclib.Server('http://localhost:8000')
        self.univers = pickle.loads(self.serveur.ConnecterJoueur(self.nom))
        self.player = self.univers.joueurs[self.nom]
        
        self.player.ajouterVaisseau(50,50,self.BatemeVaisseau())
        self.vue.zoneJeu.nouveauVaisseau(self.player.getVaisseau(1))
        #self.chat = Messageur(self) #je ne pense pas que ce fichier soit necessaire a present
        self.vue.zoneJeu.initialiserSystemes(self.univers.systemes)
        self.selectione = "false"
        self.tDeplacement.start()
        self.chatMsgNbr=self.serveur.receptionMessageChat(-1) #initialise le chat

        
    def SelectionneEntite(self,event):
        #Selectionne une entite et dessine un rond autour
        #print "entite selectione"
        pass
    
    def Action(self, x, y):
        typeDeplacement = "deplacement"
        if typeDeplacement == "deplacement":     
            self.player.getVaisseau(1).xArrivee = x
            self.player.getVaisseau(1).yArrivee = y
        
    def RefreshDeplacement(self):
        # pour entrer danss cette fonction continuellement
        self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.tDeplacement.start()
        self.UpdateDictionnaireJoueurs()
        self.SendNewDeplacement()
        self.GetMessage()
        self.receptionMessageChat() #ligne qui sert au chat, placee ici en attendant
        
    def GetMessage(self):
        print self.nom
         
        self.mes1 = self.serveur.requeteClient(self.nom)
        if self.mes1 == "rien":
            pass
        else:
            self.DecodeMessage(pickle.loads(self.mes1))
        
        
    def UpdateDictionnaireJoueurs(self):
        listeNouveauJoueurs = pickle.loads(self.serveur.checkNouveauxJoueurs(self.univers.joueurs.keys()))
        if len(listeNouveauJoueurs) > 0:
            for i in range (len(listeNouveauJoueurs)):
                nom = listeNouveauJoueurs[i].id
                self.univers.joueurs[nom] = listeNouveauJoueurs[i]
      
    def SendNewDeplacement(self):
        for i in range(len(self.player.vaisseaux)):
            self.player.getVaisseau(i+1).deplacer()
            self.vue.zoneJeu.deplacerVaisseau(self.player.getVaisseau(i+1))
            self.serveur.MiseAJourVaisseaux(self.nom, pickle.dumps(self.univers.joueurs[self.nom].vaisseaux))

    
    def RefreshVue(self,NomduJoueur):
        for i in range (len(self.univers.joueurs[NomduJoueur].vaisseaux)):
            unVaisseau = self.univers.joueurs[NomduJoueur].getVaisseau(i+1)
            if self.vue.zoneJeu.existe(unVaisseau.id) <= 0:
                self.vue.zoneJeu.nouveauVaisseau(unVaisseau)
            self.vue.zoneJeu.deplacerVaisseau(unVaisseau)
    
    def TypeAction(self,x,y):
        #"deplacement" pour test, cette fonction verifiera le type
        #a passer en parametre a self.action
        self.Action(x,y)
        
    def DecodeMessage(self,listeDesMessages):
        if len(listeDesMessages) > 0:           
            for i in listeDesMessages:
                messageADecoder = listeDesMessages.pop()
                if (messageADecoder[1] == "vai"):
                    self.univers.joueurs[messageADecoder[0]].vaisseaux = messageADecoder[2]
                    self.RefreshVue(messageADecoder[0])
            
    #nomme un vaisseau, premiere lettre v pour vaisseau + nom du jouer + un id   
    def BatemeVaisseau(self):
        numero = len(self.player.vaisseaux)+1
        return "v" + self.player.id+str(numero)
            
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
            
    #####################################################
    #debut methodes chat

    def distributionMessageChat(self, message):
        self.serveur.distributionMessageChat(self.nom, message)

    def receptionMessageChat(self):
        #-1 est un nombre magique qui signifie que je demande le numero du dernier message envoye.
        #si le chiffre est different de -1, c'est le numero du message que l'on demande.
        self.chatMsgActuel = self.serveur.receptionMessageChat(-1)
        if self.chatMsgActuel > self.chatMsgNbr:
            for a in range (self.chatMsgNbr, self.chatMsgActuel):#demande les nouveaux message 1 par 1
                self.messageChat = self.serveur.receptionMessageChat(a)
                self.messageFormate = self.messageChat[0] + ": " + self.messageChat[1]
                self.vue.chat.affiche(self.messageFormate, "mauve")
            self.chatMsgNbr = self.chatMsgActuel #incremente message recu au dernier.

    #fin methodes chat
    ###################################################



        
    def BoiteConnection(self,nomJoueur,ip,couleur=""):
        self.nom = nomJoueur
        self.ip = ip
        self.couleur = "vert"
        self.vue.demarrerJeu()
        self.ConnecterAuServeur()


        
        

if __name__=="__main__":
    controlleur = Controlleur()
