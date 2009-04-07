import xmlrpclib
from modele.Joueur import Joueur
from modele.Systeme import Systeme
from affichage import ecranGalaxie
from threading import Timer
                
class Controlleur(object):
    def __init__(self):
        self.vue=ecranGalaxie(self)
        self.systeme = Systeme(50,100)
        self.player = Joueur(self, "01", "yellow", self.systeme)
        self.player.ajouterVaisseau(50, 50)
        #self.t = Timer(0.5, self.sendNewDeplacement)
        #self.sendNewDeplacement()
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        self.vue.root.mainloop()

    
    def clickEvent(self,event):
        print self.player.vaisseaux[0].xArrivee
        self.player.vaisseaux[0].xArrivee = event.x
        self.player.vaisseaux[0].yArrivee = event.y
        self.player.vaisseaux[0].deplacer
        print self.player.vaisseaux[0].xArrivee

    def sendNewDeplacement(self):
        print "entre"
        


controlleur = Controlleur()
