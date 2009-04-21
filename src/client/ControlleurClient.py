#!/usr/bin/env python

#Ce client teste la communication avec le serveur.

import xmlrpclib
import cPickle as pickle
from threading import Timer

from modele import *
from client.Vue import Vue


adresse_serveur = 'http://127.0.0.1:8000'
serveur = xmlrpclib.Server(adresse_serveur)

class Client(object):
    def __init__(self):
        #serveur.connecterJoueur("benoit") #xmlrpclib.Fault: <Fault 1: "<type 'exceptions.TypeError'>:cannot marshal None unless allow_none is enabled">
        self.orion = pickle.loads(serveur.pushSystemes().data)
        self.vue = Vue(self)
        self.selectione = "false" 
        self.joueur = self.orion.joueurs["benoit"]
        self.joueur.ajouterVaisseau(50,50)
        self.chat = Messageur(self)
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement)
        self.tDeplacement.start()
        self.vue.root.mainloop()
        self.tDeplacement.cancel()
        
        #self.orion.tabarnakTest("benoit")
        #self.orion.ajouterJoueur("benoit")

    #cette methode teste le chat
        
    def testChat(self):
        self.noMsg = 0
        #j'emvoie des messages bidons
        #serveur.addMessage("chryana","allo")
        #serveur.addMessage("michel","byebye!")
        serveur.addMessage("benoit","salut")

        self.currentMessage()


    '''
    cette methode retourne le numero du dernier message du serveur
    si ce nombre est superieur au numero actuel du message imprime,
    le client demande les messages restants.
    '''
    def currentMessage(self):
        self.pending = serveur.currentMessage()
        for x in range(self.noMsg, self.pending):
            self.returnMessage(x)
        self.noMsg = self.pending

    #affiche um message.
    def returnMessage(self, noMsg):
        self.message = serveur.returnMessage(noMsg)
        print self.message[0] + ":" + self.message[1]
            
    def clickEvent(self,event):
        #ajouter un if pour savoir si il y a quelque chose a selectionner
        if event.num == 1: 
            if self.selectione == "false":  
                self.selectionneEntite(event)
                #remplacer les events par le cadre de l'objet selectionne
                self.vue.zoneJeu.rondSelection = self.vue.zoneJeu.create_oval(event.x-10,event.y-15,event.x+15,event.y+15, outline="red",width=2) 
                self.selectione = "true"
            else:
                self.vue.zoneJeu.delete(self.vue.zoneJeu.rondSelection)
                self.selectione = "false"
            
            self.vue.zoneJeu.deleteCroix()
        elif event.num == 3:
            self.action(event)
            self.vue.zoneJeu.deleteCroix()
            self.vue.zoneJeu.drawCroix(event)      
        #print event.num
        
    def selectionneEntite(self,event):
        print "entite selectione"
        
    def action(self,event):
        self.joueur.vaisseaux[0].xArrivee = event.x
        self.joueur.vaisseaux[0].yArrivee = event.y
        
    def sendNewDeplacement(self):
        #print "sync deplacement"
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement) 
        self.tDeplacement.start()
        #eventuellement mettre un while pour tous les vaisseaux
        self.vue.zoneJeu.deleteVaisseau()
        self.joueur.vaisseaux[0].deplacer() 
        x = self.joueur.id,self.joueur.vaisseaux[0].x
        y = self.joueur.id,self.joueur.vaisseaux[0].y
        #self.vue.zoneJeu.drawVaisseau(self.joueur.vaisseaux[0].x, self.joueur.vaisseaux[0].y)
        '''
        serveur.updadeModeleDeplacement(self.joueur.id,0,x,y)
        mes = serveur.getMessage
        print mes[0]
        print mes[1]
        print mes[2]
        print mes[3]
        '''
class Messageur(object):
    def __init__(self,parent):
        self.parent=parent
        self.nom=""
        self.message=""
        self.dernierEnvoie=""
        
    def sendMessage(self, message):
        self.nom = str(self.parent.joueur.id)
        laLigne = self.nom +": " + message
        #rouge, bleu, cyan, vert, jaune, orange, brun, gris, blanc, mauve, ou rien du tout
        
        liste = pickle.loads(serveur.pushMessages(laLigne))
        i = 0
        for i in range (len(liste)):
            self.parent.vue.chat.affiche(liste[i], "mauve")
        
        
        

#unclient = Client()
#unclient.testChat()
