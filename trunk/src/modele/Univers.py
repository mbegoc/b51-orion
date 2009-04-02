#l'univers
class Univers(object):
    def __init__(self):
        self.joueurs = []
        self.systemes = []
        
    def ajouterJoueur(self):
        vaisseaux = []
        self.joueurs.append(vaisseaux)
        return len(self.joueurs)-1
        
    def ajouterVaisseau(self, joueur, vaisseau):
        self.joueurs[joueur].append(vaisseau)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)
