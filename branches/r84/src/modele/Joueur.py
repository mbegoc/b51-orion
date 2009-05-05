from modele.Vaisseau import Vaisseau

class Joueur(object):
    def __init__(self, parent, id, couleur, systInit, chatnbrMessage):
        self.parent=parent
        self.couleur = couleur
        self.id = id
        self.vaisseaux = []
        self.systemes = []
        self.ajouterSysteme(systInit)
        self.message = []
        self.chatnbrMessage = chatnbrMessage
        self.ressources = Ressources(10)
        
    def ajouterSysteme(self, systeme):
        self.systemes.append(systeme)      
    
    def ajouterVaisseau(self, posX, posY):
        self.vaisseaux.append(Vaisseau(posX,posY))
             
    '''calcul de la production des ressources de maniere globale
    C'EST RESSOURCES SONT UNIQUEMENT LES RESSOURCES GLOBALES'''
    def exploiterRessources(self):
        for systeme in self.systemes:
            ressources.additionner(systeme.ressourcesProduites())
    
    '''calcul la consommation des ressources de maniere globale
    C'EST RESSOURCES SONT UNIQUEMENT LES RESSOURCES GLOBALES'''
    def calculerRessourcesConsommees(self):
        for systeme in self.systemes:
            ressources.consommer(systeme.calculerRessourcesConsommees())
        for vaisseau in self.vaisseaux:
            ressources.consommer(vaisseau.ressourcesEntretien)
        '''il va falloir potentiellement ajouter ici la consommation pour tout
         autre objet qui consommerait des ressources'''
