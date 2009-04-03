import xmlrpclib
from modele.Joueur import Joueur
import affichage
                
class Controlleur(object):
    def __init__(self):
        self.vue=affichage.ecranGalaxie(self)
        self.player = Joueur(self, "01", "yellow", "system1")
        self.player.ajouterVaisseau(50, 50)
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        #self.vue.root.mainloop()
        
        
        
    def clickEvent(self,event):
        print "entre"
        #print self.player.vaisseaux[0].x
        #self.player.vaisseaux[0].xArrivee = event.x
        
        


controlleur = Controlleur()
