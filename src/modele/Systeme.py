from modele.Ressources import Ressources
from modele.Infrastructure import Infrastructure
# un systeme stellaire
# un systeme stellaire a une position fixe 
# dans l'espace est ne fait pas grand chose a part ca
class Systeme(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        #ressources potentiellement produites dans un systeme
        self.ressourcesPotentielles = Ressources(1)
        #les ressources locales au systeme
        self.ressources = Ressources(0)
        
        self.infrastructures = []
        
    def ajouterInfrastructure(self, infrastructure):
        self.infrastructures.append(infrastructure)
        
    '''IL MANQUE ENCORE LA DIFFERENCIATION ENTRE LES RESSOURCES LOCALES ET GLOBALES'''
    def exploiterRessources(self):
        ressourcesProduites = self.ressourcesPotentielles.copier()
        for infrastucture in self.infrastructures:
            ressourcesProduites.multiplier(infrastructure.modificateurRessources)
        return ressourcesProduites
    
    '''IL MANQUE ENCORE LA DIFFERENCIATION ENTRE LES RESSOURCES LOCALES ET GLOBALES'''
    def calculerRessourcesConsommees(self):
        ressourcesConsommees = Ressources()
        for infrastucture in self.infrastructures:
            ressourcesConsommees.additionner(infrastructure.ressourcesEntretien)
        return ressourcesConsommees

if __name__ == "__main__":
    systeme = Systeme(0, 0)
    infrastructure = Infrastructure("extracteur")
    infrastructure.ressourcesEntretien.energie = 10
    infrastructure.modificateurRessources.metaux = 20
    systeme.ajouterInfrastructure(infrastructure)
    print systeme.exploiterRessources().toList()
    print systeme.calculerRessourcesConsommees().toList()
    