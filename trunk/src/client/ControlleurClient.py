import xmlrpclib
from modele.Joueur import Joueur
from modele.Systeme import Systeme
from threading import Timer
from Vue import Vue
                
class Controlleur(object):
    def __init__(self):
        self.vue=Vue(self)
        self.systeme = Systeme(50,100)
        self.player = Joueur(self, "01", "yellow", self.systeme)
        self.player.ajouterVaisseau(50, 50)
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement)
        self.tDeplacement.start()
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        self.vue.root.mainloop()
        self.tDeplacement.cancel()

    def clickEvent(self,event):
        if event.num == 1:
            self.selectionneEntite(event)
        elif event.num == 3:
            self.action(event)
        print event.num
            
    def selectionneEntite(self,event):
        print "entite selectione"
    
    def action(self,event):
        print self.player.vaisseaux[0].xArrivee
        self.player.vaisseaux[0].xArrivee = event.x
        self.player.vaisseaux[0].yArrivee = event.y
        self.player.vaisseaux[0].deplacer
        print self.player.vaisseaux[0].xArrivee
        
        
        
    def EtatAttaque(self):
        print "sync etat attaque"
        
    def sendNewDeplacement(self):
        print "sync deplacement"
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement) # pour entrer danss cette fonction continuellement
        self.tDeplacement.start()
        #self.serveur.player.vaisseaux= self.joueur.vaisseaux
        
    def refresh(self):
        print "sync serveur"
        


controlleur = Controlleur()
