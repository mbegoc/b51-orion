#l'univers
class Univers(Object):
    def __init__(self):
        self.tailleX=500
        self.tailleY=600
        self.joueurs = []
        self.systemes = []
        self.couleursJoueurs=["blue","green","purple","orange","yellow","red"]    # Une couleur pour chaque joueur
        
    def ajouterJoueur(self,id):
        couleur=self.couleursJoueurs.pop()
        system=self.systemes.pop()
        self.joueurs[id]=Joueur(self,id,couleur,system)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)