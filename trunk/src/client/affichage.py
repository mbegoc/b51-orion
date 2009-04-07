#!/usr/bin/env python

from Tkinter import *

###this should be part of Controler
#import xmlrpclib
#
#server='http://chryana.bounceme.net:6900'
#talkServer = xmlrpclib.ServerProxy(server) 


class ecranGalaxie:
    def __init__(self,parent):
        self.parent = parent #parent étant le controlleur
        self.root=Tk()
        self.root.title("Master of Orion")

        self.largeur=500
        self.hauteur=600

        lecanevas=Canvas(self.root,width=self.largeur, height=self.hauteur, bg="black")#fix this
        allo=Dessin(lecanevas,self)


class Dessin:
    def __init__(self, canevas,parent):
        self.parent=parent #parent étant ecranGalaxie

        canevas.bind("<Button-1>", self.parent.parent.clickEvent) #envoie l'objet event au controlleur


        canevas.pack(side=TOP)

        ########to delete
        ##section affichage d'elements avec un element statique pour le moment. eventuellement, recevra une liste d'objets a afficher a l'ecran.
        planete=canevas.create_oval(100, 100, 105, 105, fill="white")

        


    #def sendPosition(self,event): #envoie la coordonnee de la souris au controleur
        #parent.sPosition(event.x,event.y)
        #print event.x
        #print event.y

#x=ecranGalaxie()





