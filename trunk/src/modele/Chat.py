#/usr/bin/env python

#ce fichier gere le chat

import time

class Chat(object):
    def __init__(self):
        self.chatlog = open("chatlog.txt", "w")
        self.nbrMessage = 0

        #les messages sont stockes dans un dictionnaire.
        #la position 0 contient le nom de la personne qui a envoye le message
        #la position 1 contient le message en tant que tel.
        self.nick = 0
        self.msg = 1


        self.messages={}


    def ajouterMessage(self, nick, message):
        self.messages[self.nbrMessage]=[nick, message]

        
        #ecrit le chat dans le log
        self.chatlog.write(time.strftime("%H:%M:%S", time.localtime()) + " <" + self.messages[self.nbrMessage][self.nick] + "> " + self.messages[self.nbrMessage][self.msg] + "\n")

        #debug
        #print self.nicks[self.nbrMessage] + ":" + self.messages[self.nbrMessage]

        self.nbrMessage = self.nbrMessage + 1


    def messageActuel(self):
        return self.nbrMessage

    def renvoieMessage(self, numeroMsg):
        return self.messages[numeroMsg]
        


    def terminerChat(self):
        self.chatlog.close()
