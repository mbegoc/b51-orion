class Messageur(object):
    def __init__(self,parent):
        self.parent=parent
        self.nom=""
        self.message=""
        self.dernierEnvoie=""
        
    def sendMessage(self, message):
        self.nom = "Joueur" + str(self.parent.player.id)
        laLigne = self.nom +": " + message
        #rouge, bleu, cyan, vert, jaune, orange, brun, gris, blanc, mauve, ou rien du tout
        self.parent.vue.chat.affiche(laLigne, "mauve")