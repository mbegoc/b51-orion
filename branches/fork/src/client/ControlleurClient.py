import xmlrpclib
from modele.Joueur import Joueur
from modele.Systeme import Systeme
from threading import Timer
from Vue import Vue
                
class Controlleur(object):
    def __init__(self):
        self.serveur = xmlrpclib.ServerProxy('http://localhost:8000')
        #pourquoi "Benoit" fonctionne pas et 01 oui??
        self.univers = self.serveur.ConnecterJoueur("01")
        #remplacer le 0 par un random in range liste systemes
        self.player = Joueur(self, "01", "yellow", self.univers.systemes[0].id)
        self.univers.systemes[0].conquerant = "01"
        self.chat = Messageur(self)
        self.vue=Vue(self)
        
    
        self.player.ajouterVaisseau(50, 50)
        # a mettre dans les entite
        self.selectione = "false" 
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement)
        self.tDeplacement.start()
        
        self.vue.root.mainloop()
        self.tDeplacement.cancel()

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
            
        print event.num
        
            
    def selectionneEntite(self,event):
        print "entite selectione"
    
    def action(self,event):
        self.player.vaisseaux[0].xArrivee = event.x
        self.player.vaisseaux[0].yArrivee = event.y
        
        
    def EtatAttaque(self):
        print "sync etat attaque"
        
    def sendNewDeplacement(self):
        #print "sync deplacement"
        self.tDeplacement = Timer(0.5, self.sendNewDeplacement) 
        self.tDeplacement.start()
        #eventuellement mettre un while pour tous les vaisseaux
        self.player.vaisseaux[0].deplacer() 
        self.serveur.requeteClient(self.player.id)
        
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
        #rouge, bleu, cyan, vert, jaune, orange, brun, gris, blanc, mauve, ou rien du tout
        self.parent.vue.chat.affiche(laLigne, "mauve")
        
        

if __name__=="__main__":
    controlleur = Controlleur()
