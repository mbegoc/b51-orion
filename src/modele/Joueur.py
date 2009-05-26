from modele.Vaisseau import Vaisseau
from modele.Ressources import Ressources

class Joueur(object):
    def __init__(self, parent, id, couleur, systInit):
        self.parent=parent
        self.couleur = couleur
        self.id = id
        self.vaisseaux = {}
        self.systemes = []
        self.ajouterSysteme(systInit)
        self.message = []
        
        self.ressources = Ressources(10).getRessourcesGlobales()
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)      
    
    def ajouterVaisseau(self, posX, posY, id):
        self.vaisseaux[id] = Vaisseau(self,posX,posY, id)
        
    def getVaisseau(self,id):
        key = "v" + self.id + str(id)
        return self.vaisseaux[key]
             
    '''calcul de la production des ressources
    CES RESSOURCES SONT UNIQUEMENT LES RESSOURCES GLOBALES'''
    def exploiterRessources(self):
        for systeme in self.systemes:
            self.ressources.additionner(systeme.exploiterRessources())
        #return self.ressources
    
    '''calcul la consommation des ressources de maniere globale
    C'EST RESSOURCES SONT UNIQUEMENT LES RESSOURCES GLOBALES'''
    def calculerRessourcesConsommees(self):
        for systeme in self.systemes:
            self.ressources = (systeme.calculerRessourcesConsommees(self.ressources))
        ''' je m'etais dit qu'on calculerait ici la consommation des vaisseaux, mais ca pose des problemes logiques
        il vaut mieux que les vaisseaux emporte avec eux les ressources dont ils ont besoin pour fonctionner'''
        #for vaisseau in self.vaisseaux:
        #    self.ressources.consommer(vaisseau.ressourcesEntretien)
        '''il va falloir potentiellement ajouter ici la consommation pour tout
         autre objet qui consommerait des ressources'''
        #return self.ressources



###       TEST        ###
if __name__ == "__main__":
    from modele.Systeme import Systeme
    from modele.Infrastructure import Infrastructure

    '''creation d'un premier systeme particulierement riche en nourriture et assez riche en energie'''
    systeme1 = Systeme(0, 0)
    systeme1.ressourcesPotentielles.energie = 2
    systeme1.ressourcesPotentielles.nourriture = 4
    infrastructure = Infrastructure("centrale solaire")
    infrastructure.ressourcesEntretien.metaux = 2
    infrastructure.modificateurRessources.energie = 3
    systeme1.ajouterInfrastructure(infrastructure)

    '''creation d'un second systeme plutot riche en metaux'''
    systeme2 = Systeme(50, 50)
    systeme2.ressourcesPotentielles.metaux = 3
    systeme2.ressourcesPotentielles.energie = 1
    systeme2.ressourcesPotentielles.gaz = 0
    infrastructure = Infrastructure("extracteur")
    infrastructure.ressourcesEntretien.energie = 2
    infrastructure.modificateurRessources.metaux = 10
    systeme2.ajouterInfrastructure(infrastructure)
    
    joueur = Joueur("", "", "", systeme1, 0)
    joueur.ajouterSysteme(systeme2)
    joueur.ajouterVaisseau(50, 50, "id")

    #une 
    for i in range(1,20):
        joueur.exploiterRessources()
        print "ressources globales apres exploitation: ",joueur.ressources.toList()
        joueur.calculerRessourcesConsommees()
        for systeme in joueur.systemes:
            print "ressources systemes: ",systeme.ressources.toList()
            for infra in systeme.infrastructures:
                print infra.type, ": ", infra.actif
        print ""

