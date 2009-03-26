class Univers(Object):
    def __init__(self, x, y):
        self.vaisseaux = []
        self.systemes = []
        
    def ajouterVaisseau(self, vaisseau):
        self.vaisseaux.append(vaisseau)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)