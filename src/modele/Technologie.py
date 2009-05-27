class Technologie(object):
    def __init__(self,branche,nom,prix,type,bonus,requis = None):
        self.branche = branche
        self.prix = prix
        self.nom = nom
        self.type = type
        self.bonus = bonus
        self.requis = requis
        #rajouter un champ description pour l'affichage au joueur