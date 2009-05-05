def distributionMessageChat(self, message):
    self.serveur.distributionMessageChat(self.nom, message)


def receptionMessageChat(self):
    #contient un tuple de deux strings ["nick", "message"]
    self.messageChat = self.serveur.receptionMessageChat(self.nom)

    if self.messageChat[0] != "nobody":
        self.messageFormate = self.messageChat[0] + ": " + self.messageChat[1]
        self.vue.chat.affiche(self.messageFormate, "mauve")

