class Ressources(object):
    def __init__(self, default = 0):
        #les 6 ressources de base
        self.nourriture = default
        self.gaz = default
        self.metaux = default
        self.energie = default
        self.credit = default
        self.connaissance = default
        self.production = default
        
        
    def multiplier(self, ressources):
        self.nourriture = self.nourriture * ressources.nourriture
        self.gaz = self.gaz * ressources.gaz
        self.metaux = self.metaux * ressources.metaux
        self.energie = self.energie * ressources.energie 
        self.credit = self.credit * ressources.credit
        self.connaissance = self.connaissance * ressources.connaissance 
        self.production = self.production * ressources.production
        
        if self.nourriture<0 or self.connaissance<0 or self.gaz<0 or self.energie<0 or self.credit<0 or self.metaux<0:
            return 0
        else:
            return 1

    def additionner(self, ressources):
        self.nourriture = self.nourriture + ressources.nourriture
        self.gaz = self.gaz + ressources.gaz
        self.metaux = self.metaux + ressources.metaux
        self.energie = self.energie + ressources.energie 
        self.credit = self.credit + ressources.credit
        self.connaissance = self.connaissance + ressources.connaissance 
        self.production = self.production + ressources.production 
        
        if self.nourriture<0 or self.connaissance<0 or self.gaz<0 or self.energie<0 or self.credit<0 or self.metaux<0 or self.production<0:
            return 0
        else:
            return 1

    #retrancher des ressources consommees
    def consommer(self, ressources):
        self.nourriture = self.nourriture - ressources.nourriture
        self.gaz = self.gaz - ressources.gaz
        self.metaux = self.metaux - ressources.metaux
        self.energie = self.energie - ressources.energie 
        self.credit = self.credit - ressources.credit
        self.connaissance = self.connaissance - ressources.connaissance 
        self.production = self.production - ressources.production 
        if self.nourriture<0 or self.connaissance<0 or self.gaz<0 or self.energie<0 or self.credit<0 or self.metaux<0 or self.production<0:
            return 0
        else:
            return 1
        
    #cette fonction renvoie un dictionnaire de donnees. Pas d'importance fonctionnelle, facilite juste l'affichage pour le debuggage
    def toList(self):
        liste = {}
        liste["nourriture"] = (self.nourriture)
        liste["gaz"] = (self.gaz)
        liste["metaux"] = (self.metaux)
        liste["energie"] = (self.energie)
        liste["credit"] = (self.credit)
        liste["connaissance"] = (self.connaissance)
        liste["production"] = (self.production)
        return liste
    
    #duplique l'objet, si on a besoin de faire des calculs sur une ressources sans la modifier
    def copier(self):
        copie = Ressources()
        copie.nourriture = self.nourriture
        copie.gaz = self.gaz
        copie.metaux = self.metaux
        copie.energie = self.energie 
        copie.credit = self.credit
        copie.connaissance = self.connaissance 
        copie.production = self.production 
        return copie
    
    #renvoie seulement les ressources globales - pour simplifier le code des calculs de consommation et d'exploitation
    def getRessourcesGlobales(self):
        ressourcesGlobales = Ressources()
        ressourcesGlobales.credit = self.credit
        ressourcesGlobales.connaissance = self.connaissance
        return ressourcesGlobales
    
    #renvoie seulement les ressources locales - pour simplifier le code des calculs de consommation et d'exploitation
    def getRessourcesLocales(self):
        ressourcesLocales = Ressources()
        ressourcesLocales.metaux = self.metaux
        ressourcesLocales.nourriture = self.nourriture
        ressourcesLocales.energie = self.energie
        ressourcesLocales.gaz = self.gaz
        ressourcesLocales.production = self.production
        return ressourcesLocales