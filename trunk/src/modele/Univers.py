#l'univers
class Univers(Object):
    def __init__(self):
        self.tailleX=500
        self.tailleY=600
        self.joueurs = []
        self.systemes = []
        self.couleurscivs=["blue","green","purple","orange","yellow", "red"]    # Une couleur pour chaque joueur
        ## creer 10 systemes
        
    def ajouterJoueur(self):
        vaisseaux = []
        self.joueurs.append(vaisseaux)
        return len(self.joueurs)-1
        
#    def ajouterVaisseau(self, joueur, vaisseau): ## Les vaisseaux appartienent aux joueurs
#        self.joueurs[joueur].append(vaisseau)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)