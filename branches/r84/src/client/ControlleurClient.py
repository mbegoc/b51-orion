import xmlrpclib
import cPickle as pickle
from threading import Timer
import re
from modele import *
from Vue import Vue
import time
import random


class Controlleur(object):
    def __init__(self):
        self.vue=Vue(self)
        self.nom = None
        self.couleur = None
        self.ip = None
        self.serveur = None
        self.univers = None
        self.player = None
        self.gestionDev = None
        self.objetSelectionne = ""
        self.objetCible = ""
        self.messageADecoder = None
        #self.tDeplacement = Timer(0.5, self.RefreshDeplacement)
        self.vue.root.mainloop()
        #self.tDeplacement.cancel()
            
    def ConnecterAuServeur(self):
        self.serveur = xmlrpclib.Server('http://127.0.0.1:8000')
        self.univers = pickle.loads(self.serveur.ConnecterJoueur(self.nom))
        self.player = self.univers.joueurs[self.nom]
        self.gestionDev = GestionDev.GestionDev(self)
        self.vue.zoneJeu.initialiserSystemes(self.univers.systemes)
        
#        self.univers.systemes["s1"].infrastructures.append(Infrastructure.Infrastructure("fdsa"))
#        self.univers.systemes["s1"].infrastructures[0].modificateurRessources.nourriture = 2
#        self.univers.systemes["s1"].infrastructures[0].modificateurRessources.connaissance = 2
#        self.univers.systemes["s1"].infrastructures[0].ressourcesEntretien.energie = 2
#        self.player.systemes.append(self.univers.systemes["s1"])
#        self.univers.systemes["s1"].owner = self.player.id

#        self.player.ajouterVaisseau(50,50,self.BatemeVaisseau())
#        self.vue.zoneJeu.nouveauVaisseau(self.player.getVaisseau(1), self.player.couleur, reference = 1)
#        self.player.ajouterVaisseau(100,100,self.BatemeVaisseau())
#        self.player.getVaisseau(2).classe="militaire"
#        self.player.getVaisseau(2).vitesse = 10
#        self.vue.zoneJeu.nouveauVaisseau(self.player.getVaisseau(2), self.player.couleur)
        systemeId = self.univers.systemes.keys()[random.randint(0, len(self.univers.systemes))]
        x = random.randint(-100, 101)
        y = random.randint(-100, 101)
        test = {}
        x += self.univers.systemes[systemeId].x
        y += self.univers.systemes[systemeId].y
        self.player.ajouterVaisseau(x,y,self.BatemeVaisseau())
        self.player.getVaisseau(1).classe="drone"
        self.player.getVaisseau(1).vitesse = 2
        self.vue.zoneJeu.nouveauVaisseau(self.player.getVaisseau(1), self.player.couleur)

        #self.tDeplacement.start()
        self.vue.root.after(100, self.RefreshDeplacement)
        self.calculerRessources()
        self.chatMsgNbr=self.serveur.receptionMessageChat(-1) #initialise le chat

        
    def SelectionneEntite(self,event):
        pass
    
    def Action(self, x, y):
        typeDeplacement = "deplacement"
        if typeDeplacement == "deplacement":
            self.getVaisseau(self.objetSelectionne).xArrivee = x
            self.getVaisseau(self.objetSelectionne).yArrivee = y
#            self.player.vaisseaux[].xArrivee = x
#            self.player.vaisseaux[self.objetSelectionne].yArrivee = y
        
    def RefreshDeplacement(self):
        debug = ""
        debut= time.time()
        self.UpdateDictionnaireJoueurs()
        debug += "UpdateDictionnaireJoueurs: "+str(time.time() - debut)+"\n"
        top = time.time()
        self.SendNewDeplacement()
        debug += "SendNewDeplacement: "+str(time.time() - top)+"\n"
        top = time.time()
        self.GetMessage()
        debug += "GetMessage: "+str(time.time() - top)+"\n"
        top = time.time()
        self.receptionMessageChat() #ligne qui sert au chat, placee ici en attendant
        debug += "receptionMessageChat: "+str(time.time() - top)+"\n"
        top = time.time()
        self.vue.rapportSelection.genererRapport(self.objetSelectionne)
        debug += "rapportSelection: "+str(time.time() - top)+"\n"
        debug += "Total: "+str(time.time() - debut)
        self.vue.zoneJeu.debugMessage(debug)
        #timer de rappel
        
        self.vue.root.after(100, self.RefreshDeplacement)
        #self.tDeplacement = Timer(0.1, self.RefreshDeplacement)
        #self.tDeplacement.start()
        
    def calculerRessources(self):
        self.player.exploiterRessources()
        self.player.calculerRessourcesConsommees()

        self.vue.root.after(5000, self.calculerRessources)
        
    def GetMessage(self):
        debug = ""
        debut= time.time()

        
        self.mes1 = self.serveur.requeteClient(self.nom)
        
        debug += "requeteClient: "+str(time.time() - debut)+"\n"
        top = time.time()
        
        if self.mes1 == "rien":
            pass
        else:
            self.DecodeMessage(pickle.loads(self.mes1))

        self.vue.rapportSelection.genererRapport(self.objetSelectionne)
        debug += "depickle: "+str(time.time() - top)+"\n"
        #print self.mes1 #commente parce que remplit la console et que je veux m'en servir pour lire autre chose

        debug += "Total: "+str(time.time() - debut) 
        #self.vue.zoneJeu.debugMessage(debug)
            
    def getVaisseau(self, idVaisseau):
        for joueur in self.univers.joueurs:
            if re.search(self.univers.joueurs[joueur].id+"\d*$", idVaisseau):
                return self.univers.joueurs[joueur].vaisseaux[idVaisseau]
        return ""
            
    def getSysteme(self, idSysteme):
        return self.univers.systemes[idSysteme]
    
    def ciblerObjet(self, objetCible):
        self.objetCible = objetCible
        vaisseau = self.getVaisseau(self.objetSelectionne)
        if vaisseau:
            vaisseau.idDestination = objetCible
        
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
            self.player.getVaisseau(i+1).securiser()
        
        self.serveur.MiseAJourVaisseaux(self.nom, pickle.dumps(self.univers.joueurs[self.nom].vaisseaux))

        for i in range(len(self.player.vaisseaux)):
            self.player.getVaisseau(i+1).desecuriser(self.player)
    
    def RefreshVue(self,NomduJoueur):
        for i in range (len(self.univers.joueurs[NomduJoueur].vaisseaux)):
            unVaisseau = self.univers.joueurs[NomduJoueur].getVaisseau(i+1)
            if self.vue.zoneJeu.existe(unVaisseau.id) <= 0:
                self.vue.zoneJeu.nouveauVaisseau(unVaisseau,self.univers.joueurs[NomduJoueur].couleur, proprietaire = 0)
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
                    for i in self.univers.joueurs[messageADecoder[0]].vaisseaux:
                        self.univers.joueurs[messageADecoder[0]].vaisseaux[i].desecuriser(self.univers.joueurs[messageADecoder[0]])
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
            
    ###----------------------------------------------------------###
    #debut methodes chat

    def distributionMessageChat(self, message):
        self.serveur.distributionMessageChat(self.nom, message)

    def receptionMessageChat(self):
        #-1 est un nombre magique qui signifie que je demande le numero du dernier message envoye.
        #si le chiffre est different de -1, c'est le numero du message que l'on demande.
        self.chatMsgActuel = self.serveur.receptionMessageChat(-1)
        if self.chatMsgActuel > self.chatMsgNbr:
            '''
            le rafraichissement de cette methode est tellement rapide que j'ai
            des problemes car la fonction est rappelee avant que la methode
            soit terminee. je vais donc changer la valeur de self.chatMsgNbr
            avant d'entrer dans la boucle pour eviter de demander plusieurs
            fois le meme message.
            '''
            self.chatLoop = self.chatMsgNbr #evite que la boucle ne soit executee plusieurs fois.
            self.chatMsgNbr = self.chatMsgActuel #incremente message recu en dernier.
            for a in range (self.chatLoop, self.chatMsgActuel):#demande les nouveaux message 1 par 1
                self.messageChat = self.serveur.receptionMessageChat(a)
                self.messageFormate = self.messageChat[0] + ": " + self.messageChat[1]
                self.vue.chat.affiche(self.messageFormate, "mauve")


    #fin methodes chat
    ###----------------------------------------------------------###
    #debut methodes combat

    def initierCombat(self, attaquant, defenseur):
        pass



    #fin methodes combat
    ###----------------------------------------------------------###






    def VerifierTech(self,nomTech):
       if nomTech in self.player.arbre:
            if self.player.ressources.connaissance >= int(self.player.arbre[nomTech].prix):
                if self.player.arbre[nomTech].requis[0] == '' or self.player.arbre[nomTech].requis in self.player.techAquise:
                    return 1  

        
    def BoiteConnection(self,nomJoueur,ip,couleur=""):
        if not re.search("\d$", nomJoueur):
            self.nom = nomJoueur
        else:
            self.vue.connexion.erreurConnexion("Le nom de joueur ne doit pas se terminer par un chiffre.")
            return
        
        self.ip = ip
        self.vue.demarrerJeu()
        self.ConnecterAuServeur()


        
        

if __name__=="__main__":
    controlleur = Controlleur()
