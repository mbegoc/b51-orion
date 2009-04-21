import xmlrpclib
from modele.Joueur import Joueur
from modele.Systeme import Systeme
from threading import Timer
from Vue import Vue
                
class Controlleur(object):
    def __init__(self):
        self.chat = Messageur(self)
        self.vue=Vue(self)
        
        self.systeme = Systeme(50,100)
        self.player = Joueur(self, "01", "yellow", self.systeme)
        self.player.ajouterVaisseau(50, 50)
        self.selectione = "false" # a mettre dans les entite
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement)
        self.tDeplacement.start()
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        self.vue.root.mainloop()
        self.tDeplacement.cancel()

    def clickEvent(self,event):
        if event.num == 1: #un autre if pour savoir si il y a quelque chose a selectionner
            if self.selectione == "false":  
                self.selectionneEntite(event)
                self.vue.zoneJeu.rondSelection = self.vue.zoneJeu.create_oval(event.x-10,event.y-15,event.x+15,event.y+15, outline="red",width=2) #remplacer les event par le cadre de l'objet selectionne
                self.selectione = "true"
            else:
                self.vue.zoneJeu.delete(self.vue.zoneJeu.rondSelection)
                self.selectione = "false"
            
            self.vue.zoneJeu.deleteCroix()
        elif event.num == 3:
            self.action(event)
            self.vue.zoneJeu.deleteCroix()
            self.vue.zoneJeu.drawCroix(event)
            
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
        #print "sync deplacement"
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement) # pour entrer danss cette fonction continuellement
        self.tDeplacement.start()
        #self.serveur.player.vaisseaux= self.joueur.vaisseaux
        
    def refresh(self):
        print "sync serveur"
        
class Messageur(object):
    def __init__(self,parent):
        self.parent=parent
        self.nom=""
        self.message=""
        self.dernierEnvoie=""
        
    def sendMessage(self, message):
        self.nom = "Joueur" + str(self.parent.player.id)
        laLigne = self.nom +": " + message
        self.parent.vue.chat.affiche(laLigne, "mauve")#rouge, bleu, cyan, vert, jaune, orange, brun, gris, blanc, mauve, ou rien du tout
        
        

if __name__=="__main__":
    controlleur = Controlleur()
