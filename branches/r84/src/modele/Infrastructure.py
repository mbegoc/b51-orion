from modele.Ressources import Ressources

class Infrastructure(object):
    def __init__(self, type):
        self.type = type
        self.actif = 1
        
        ''' les modificateurs de ressources pourront multiplier un potentiel 
        de production de ressources. Par exemple, une centrale electrique pourrait 
        avoir une valeur de 2, ce qui multiplierait le potentiel de base d'un systeme par 2
        ces valeurs devront etre modifiees directement dans le dictionnaire'''
        self.modificateurRessources = Ressources(1)

        ''' le cout d'entretien de cette infrastructure '''
        self.ressourcesEntretien = Ressources(0)

    def produire(self, unite):
        '''cette fonction va retourner une unite (vaisseau, disciple...)
        en fonction du type d'infrastructure'''
        pass
             