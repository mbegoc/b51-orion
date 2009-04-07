import xmlrpclib
from modele.Joueur import Joueur
from modele.Systeme import Systeme
from threading import Timer
from Vue import Vue
                
class Controlleur(object):
    def __init__(self):
        self.vue=Vue()
        self.systeme = Systeme(50,100)
        self.player = Joueur(self, "01", "yellow", self.systeme)
        self.player.ajouterVaisseau(50, 50)
        self.t = Timer(0.5, self.sendNewDeplacement)
        self.t.start()
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        self.vue.root.mainloop()

    
    def clickEvent(self,event):
        print self.player.vaisseaux[0].xArrivee
        self.player.vaisseaux[0].xArrivee = event.x
        self.player.vaisseaux[0].yArrivee = event.y
        self.player.vaisseaux[0].deplacer
        print self.player.vaisseaux[0].xArrivee

    def sendNewDeplacement(self):
        print "sync deplacement"
        self.t = Timer(0.5, self.sendNewDeplacement)
        self.t.start()
        #self.serveur.player.vaisseaux= self.joueur.vaisseaux
        
    def EtatAttaque(self):
        print "sync etat attaque"
        
        


controlleur = Controlleur()
