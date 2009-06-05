#Ce fichier sert a modeliser le combat, tel que decrit dans le document "modele du combat" sur google docs.


class Combat(object):

    #les vaisseaux qui s'attaquent sont passes en parametre
    def __init__(self, attaquant, defenseur):
        pass


    def attaque(self):

        #cycle des armes de l'attaquant
        for k,v in attaquant.armes:
                
            #verification s'il existe un blindage particulier
            #pour le dommage de l'attaquant
            if v[1] in defenseur.blindage:
                self.stop = defenseur.blindage[v[1]]
            else:
                self.stop = defenseur.blindage['defaut']

                #le dommage ne peut etre negatif
                self.dommage = v[0] - self.stop
                if (v[0] - self.stop) < 0:
                    self.dommage = 0

                defenseur.dommage = defenseur.dommage + self.dommage

            #le defenseur attaque a son tour, et ce meme si ses points
            #de dommage sont superieur a 100.
            for k,v in defenseur.armes:
                
                #verification s'il existe un blindage particulier
                #pour le dommage de l'attaquant
                if v[1] in attaquant.blindage:
                    self.stop = attaquant.blindage[v[1]]
                else:
                    self.stop = attaquant.blindage['defaut']

                #le dommage ne peut etre negatif
                self.dommage = v[0] - self.stop
                if (v[0] - self.stop) < 0:
                    self.dommage = 0

                attaquant.dommage = attaquant.dommage + self.dommage


            if attaquant.dommage > 100 or defenseur.dommage > 100:
                self.termine = True

    #calcule la distance entre les deux vaisseaux, 
    #si la distance est plus petite que 5, attaque
    def confirmeAttaque(self):
        self.distance = math.sqrt(math.pow((attaquant.x - defenseur.x), 2) + math.pow((attaquant.y - defenseur.y), 2))
        if (self.distance <= 5):
            self.attaque()

