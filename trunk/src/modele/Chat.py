#/usr/bin/env python

#ce fichier gere le chat

import time

class Chat(object):
    def __init__(self):
        self.chatlog = open("chatlog.txt", "w")
        self.nbrMessage = 0

        #les noms et les messages sont separes en deux listes. je n'ai pas trouve
        #pour le moment de facon plus efficace de representer l'information...
        self.nicks = []
        self.messages =[]




    def addMessage(self, nick, message):
        self.nicks.append(nick)
        self.messages.append(message)
        
        #ecrit le chat dans le log
        self.chatlog.write(time.strftime("%H:%M:%S", time.localtime()) + " <" +self.nicks[self.nbrMessage] + "> " + self.messages[self.nbrMessage] + "\n")

        #debug
        #print self.nicks[self.nbrMessage] + ":" + self.messages[self.nbrMessage]

        self.nbrMessage = self.nbrMessage + 1


    def currentMessage(self):
        return self.nbrMessage

    def returnMessage(self, numeroMsg):
        self.transmission = self.nicks[numeroMsg], self.messages[numeroMsg]
        return self.transmission


    def terminer(self):
        self.chatlog.close()

'''
leChat = Chat()

leChat.ajouterMessage(nom, msg)
leChat.terminer()

print leChat.returnMsg(0)
'''
