class Ressources(object):
    def __init__(self, default = 0):
        self.nourriture = default
        self.connaissance = default
        self.gaz = default
        self.metaux = default
        self.energie = default
        self.credit = default
        
    def multiplier(self, ressources):
        self.nourriture = self.nourriture * ressources.nourriture
        self.connaissance = self.connaissance * ressources.connaissance 
        self.gaz = self.gaz * ressources.gaz
        self.metaux = self.metaux * ressources.metaux
        self.energie = self.energie * ressources.energie 
        self.credit = self.credit * ressources.credit

    def additionner(self, ressources):
        self.nourriture = self.nourriture + ressources.nourriture
        self.connaissance = self.connaissance + ressources.connaissance 
        self.gaz = self.gaz + ressources.gaz
        self.metaux = self.metaux + ressources.metaux
        self.energie = self.energie + ressources.energie 
        self.credit = self.credit + ressources.credit
        
    def toList(self):
        liste = []
        liste.append(self.nourriture)
        liste.append(self.connaissance)
        liste.append(self.gaz)
        liste.append(self.metaux)
        liste.append(self.energie)
        liste.append(self.credit)
        return liste
    
    def copier(self):
        copie = Ressources()
        copie.nourriture = self.nourriture
        copie.connaissance = self.connaissance 
        copie.gaz = self.gaz
        copie.metaux = self.metaux
        copie.energie = self.energie 
        copie.credit = self.credit
        return copie