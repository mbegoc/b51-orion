#!/usr/bin/env python


import xmlrpclib


adresse_serveur = 'http://127.0.0.1:8000'
serveur = xmlrpclib.Server(adresse_serveur)


class Client(object):
    def __init__(self):
        self.nick = "chryana"

        serveur.ConnecterJoueur(self.nick)
        self.testChat()

    def testChat(self):
        serveur.distributionMessageChat(self.nick, "allo1")
        serveur.distributionMessageChat(self.nick, "allo2")
        serveur.distributionMessageChat(self.nick, "allo3")

        self.message1=serveur.receptionMessageChat(self.nick)
        self.message2=serveur.receptionMessageChat(self.nick)
        self.message3=serveur.receptionMessageChat(self.nick)
        self.message4=serveur.receptionMessageChat(self.nick)

        print self.message1[0], " ", self.message1[1]
        print self.message2[0], " ", self.message2[1]
        print self.message3[0], " ", self.message3[1]
        print self.message4[0], " ", self.message4[1]








client=Client()
