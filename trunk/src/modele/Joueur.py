class Joueur(object):
    def __init__(self, parent, id, couleur, systInit):
        self.parent=parent
        self.couleur = couleur
        self.id = id
        self.vaisseaux = []
        self.systemes = []
        self.ajouterSysteme(systInit)
        self.ajouterVaisseau(systInit.posX, systInit.PosY)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)      
    
    def ajouterVaisseau(self, posX, posY):
        self.vaisseaux.append(Vaisseau(self,posX,posY))
        
  