from Vaisseau import Vaisseau

class Joueur(object):
    def __init__(self, nick, systeme):
        self.nick = nick
        self.vaisseaux={}
        self.unVaisseau = 0

        self.systemes = {}
        self.unSysteme = 0

        self.addSysteme(systeme)
        self.addVaisseau(self.systemes[0].x, self.systemes[0].y)
        #self.parent=parent
        #self.couleur = couleur
        #self.id = id
        #self.message = []
        
    def addSysteme(self, systeme):
        self.systemes[self.unSysteme] = systeme
        self.unSysteme = self.unSysteme + 1

    
    def addVaisseau(self, x, y):
        self.vaisseaux[self.unVaisseau]=Vaisseau(x, y)
        self.unVaisseau = self.unVaisseau + 1

    def moveVaisseau(self, noVaisseau, x ,y):
        self.vaisseaux[noVaisseau].moveVaisseau(x, y)
