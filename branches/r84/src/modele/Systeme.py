from modele.Ressources import Ressources
from modele.Infrastructure import Infrastructure

# un systeme stellaire
# un systeme stellaire a une position fixe 
# dans l'espace est ne fait pas grand chose a part ca
class Systeme(object):
    def __init__(self, x, y,z=0,id=""):
        #code temporaire en attendant que le controlleur appelle cette classe avec les bons parametres
        if id == "":
            self.id="s"+str(x)+str(y)
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.owner = ""
        #ressources potentiellement produites dans un systeme
        self.ressourcesPotentielles = Ressources(1)
        #les ressources locales au systeme
        self.ressources = Ressources(10).getRessourcesLocales()
        
        self.infrastructures = []
        
        self.ecouteurs = []
        
    def ajouterInfrastructure(self, infrastructure):
        self.infrastructures.append(infrastructure)
        
    '''calcul de l'exploitation et de la consommation des ressources pour ce systeme
    on differencie les ressources globales des ressources locales: 
    La fonction ne retourne que la partie globale qui servira au calcul des ressources pour le joueur'''
    def exploiterRessources(self):
        ressourcesProduitesLocalement = self.ressourcesPotentielles.copier().getRessourcesLocales()
        ressourcesProduitesGlobalement = self.ressourcesPotentielles.copier().getRessourcesGlobales()
        
        for infrastructure in self.infrastructures:
            if infrastructure.actif:
                ressourcesProduitesLocalement.multiplier(infrastructure.modificateurRessources)
                ressourcesProduitesGlobalement.multiplier(infrastructure.modificateurRessources)
            
        self.ressources.additionner(ressourcesProduitesLocalement)
        return ressourcesProduitesGlobalement
    
    def calculerRessourcesConsommees(self, ressourcesGlobales):
        for infrastructure in self.infrastructures:
                if not self.ressources.consommer(infrastructure.ressourcesEntretien.getRessourcesLocales()) or not ressourcesGlobales.consommer(infrastructure.ressourcesEntretien.getRessourcesGlobales()):
                    infrastructure.actif = 0
                    self.ressources.additionner(infrastructure.ressourcesEntretien.getRessourcesLocales())
                    ressourcesGlobales.additionner(infrastructure.ressourcesEntretien.getRessourcesGlobales())
                else:
                    infrastructure.actif = 1
        return ressourcesGlobales

        '''ca pourait etre une alternative interessante que la consommation des ressources
        renvoie les ressource REELLEMENT consommees (cas ou les ressources manquent) puis renvoie cette valeur
        ressourcesConssommees = self.ressources.consommer(ressourcesConssommees)
        return ressourcesConsommees
        '''
    def ajouterOwnerSysteme(self, vaisseau):
        if vaisseau.valideArriveSysteme() :
            self.owner=vaisseau.id[1:]
            Joueur.ajouterSysteme(vaisseau.idDestination)
            return "ok"
        else:
            return "rien"