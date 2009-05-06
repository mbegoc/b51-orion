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
        self.ressources = Ressources(10).getRessourcesLocales()
        
        self.infrastructures = []
        
    def ajouterInfrastructure(self, infrastructure):
        self.infrastructures.append(infrastructure)
        
    '''calcul de l'exploitation et de la consommation des ressources pour ce systeme
    on differencie les ressources globales des ressources locales: 
    La fonction ne retourne que la partie globale qui servira au calcul des ressources pour le joueur'''
    def exploiterRessources(self):
        ressourcesProduitesLocalement = self.ressourcesPotentielles.copier().getRessourcesLocales()
        ressourcesProduitesGlobalement = self.ressourcesPotentielles.copier().getRessourcesGlobales()
        
        for infrastructure in self.infrastructures:
            ressourcesProduitesLocalement.multiplier(infrastructure.modificateurRessources)
            ressourcesProduitesGlobalement.multiplier(infrastructure.modificateurRessources)
            
        self.ressources.additionner(ressourcesProduitesLocalement)
        return ressourcesProduitesGlobalement
    
    def calculerRessourcesConsommees(self):
        ressourcesConsommeesLocalement = Ressources()
        ressourcesConsommeesGlobalement = Ressources()
        
        for infrastructure in self.infrastructures:
            ressourcesConsommeesLocalement.additionner(infrastructure.ressourcesEntretien.getRessourcesLocales())
            ressourcesConsommeesGlobalement.additionner(infrastructure.ressourcesEntretien.getRessourcesGlobales())
        
        self.ressources.consommer(ressourcesConsommeesLocalement)
        return ressourcesConsommeesGlobalement

        '''ca pourait etre une alternative interessante que la consommation des ressources
        renvoie les ressource REELLEMENT consommees (cas ou les ressources manquent) puis renvoie cette valeur
        ressourcesConssommees = self.ressources.consommer(ressourcesConssommees)
        return ressourcesConsommees
        '''


    