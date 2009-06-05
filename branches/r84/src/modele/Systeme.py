from modele.Ressources import Ressources
from modele.Infrastructure import Infrastructure
from modele.Planete import Planete
import random

# un systeme stellaire
# un systeme stellaire a une position fixe 
# dans l'espace est ne fait pas grand chose a part ca
class Systeme(object):
    def __init__(self, parent, x, y,z,id):
        self.parent=parent
        self.x = x
        self.y = y
        self.z = z
        self.id = id
        self.owner = ""

        #ressources potentiellement produites dans un systeme
        self.ressourcesPotentielles = Ressources(1)
        #les ressources locales au systeme
        self.ressources = Ressources(10).getRessourcesLocales()
        self.planetes = {}
        self.creerPlanetes()
        self.infrastructures = []
        
        self.ecouteurs = []
    
    
    def creerPlanetes(self):
        for i in range (random.randint(0,10)):
            nom = "p" + self.id +"." + str(len(self.planetes))
            self.planetes[nom] = Planete(self,nom)
        
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
            

    def ajouterOwnerSysteme(self, vaisseau,joueur):
        if vaisseau.valideArriveSysteme() :
            self.owner=joueur.id
            joueur.ajouterSysteme(vaisseau.idDestination)
            print "Le systeme a ete ajoute"
            return "ok"
        else:
            print "Le systeme n'a pas ete ajoute"
            return "rien"
