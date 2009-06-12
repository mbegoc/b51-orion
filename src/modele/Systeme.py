from modele.Ressources import Ressources
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
        self.ressources = Ressources(0).getRessourcesLocales()
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
        ressourcesProduitesLocalement = (self.ressourcesPotentielles.copier()).getRessourcesLocales()
        ressourcesProduitesGlobalement = (self.ressourcesPotentielles.copier()).getRessourcesGlobales()
        
        for infrastructure in self.infrastructures:
            if infrastructure.actif:
                #on a besoin d'un modificateur de ressources pondere par la population
                population = Ressources(self.ressources.population)
                population.population = 1
                modificateurPonderePopulation = infrastructure.modificateurRessources.copier()
                modificateurPonderePopulation.multiplier(population)
                
                ressourcesProduitesLocalement.multiplier(modificateurPonderePopulation)
                ressourcesProduitesGlobalement.multiplier(modificateurPonderePopulation)
            
        self.ressources.additionner(ressourcesProduitesLocalement)
        return ressourcesProduitesGlobalement
    
    def calculerRessourcesConsommees(self, ressourcesGlobales):
        for infrastructure in self.infrastructures:
                #on a besoin d'un modificateur de ressources pondere par la population
                population = Ressources(self.ressources.population)
                population.population = 1
                entretienLocal = infrastructure.ressourcesEntretien.getRessourcesLocales().copier()
                entretienLocal.multiplier(population)
                entretienGlobal = infrastructure.ressourcesEntretien.getRessourcesGlobales().copier()
                entretienGlobal.multiplier(population)
                if not self.ressources.consommer(entretienLocal) or not ressourcesGlobales.consommer(entretienGlobal):
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
        print "arrive a ajouterOwner"
        if vaisseau.valideArriveSysteme() :
            self.owner=joueur.id
            joueur.ajouterSysteme(vaisseau.idDestination)
            print "********"
            print "Le systeme a ete ajoute"
            print "********"
        else:
            print "********"
            print "Le systeme n'a pas ete ajoute"
            print "********"
            