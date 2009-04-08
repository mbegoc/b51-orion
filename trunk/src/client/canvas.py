#!/usr/bin/env python

from Tkinter import *
import glob, os

class ZoneDeJeu(Canvas):
    def __init__(self, parent):
        #appel au constructeur de la super classe
        Canvas.__init__(self, parent.root, width=1000, height=600, background="#000000", scrollregion=(0, 0, 2000, 2000))
        #on garde une reference vers la classe parent
        self.parent = parent
        self.rondSelection = None # rond autour de l'entite selectionne
        self.croix1 = None # x qui represente le cible de deplacement ou d'attaque besoin de 2 lignes
        self.croix2 = None
        #initialisation des images disponibles
        self.images = {}
        ZoneDeJeu.__genererImages__(self)

        self.create_line(0, 0, 2000, 2000, fill="#ffffff")
        self.create_line(2000, 0, 0, 2000, fill="#ffffff")


        self.bind("<Button-1>", self.parent.parent.clickEvent) #envoie l'objet event au controlleur
        self.bind("<Button-3>", self.parent.parent.clickEvent) #envoie l'objet event au controlleur

    #cette fonction ne sert qu'a 
    def dessinerImage(self, nom, x, y):
        if nom in self.images:
            self.create_image(x, y, image=self.images[nom], tags=nom)
            return 1
        else:
            return 0

    '''ATTENTION: cette fonction doit imperativement etre appelee a travers la classe de l'objet, par par l'objet lui meme (ZoneDeJeu.__genererImages__(objet) )
    Je ne sais pas pourquoi, mais si l'image est generee dans l'objet sur lequel elle va etre affichee, ca ne marche pas. Il faut donc appeler cette methode
    sur la classe et passer en parametre l'instance d'un ZoneDeJeu dans lequel la liste d'images sera cree'''
    #genere un dictionnaire des images contenues dans le repertoire images. La clef utilisee comme entree du dictionnaire est le nom de base du fichier (sans extension)
    def __genererImages__(instance):
        for image in glob.glob("images/*"):
            photo = PhotoImage(file=image)
            key = os.path.splitext(os.path.split(image)[1])[0]
            instance.images[key] = photo

    def representerJeu(self):
        self.dessinerImage("abasourdi", 115, 100)
        self.dessinerImage("clindoeil", 65, 100)
        self.dessinerImage("confus", 50, 170)
        self.dessinerImage("etonne", 70, 190)
        self.dessinerImage("larme", 90, 190)
        self.dessinerImage("ricane", 110, 190)
        self.dessinerImage("yeux-barres", 130, 170)
        
    def deleteJeu(self):
        self.delete("abasourdi")
        self.delete("clindoeil")
        self.delete("confus")
        self.delete("etonne")
        self.delete("larme")
        self.delete("ricane")
        self.delete("yeux-barres")
        
    def moveJeu(self):
        self.move("abasourdi", 5, 5)
        self.move("clindoeil", 5, 5)
        self.move("confus", 5, 5)
        self.move("etonne", 5, 5)
        self.move("larme", 5, 5)
        self.move("ricane", 5, 5)
        self.move("yeux-barres", 5, 5)
        
    def drawCroix(self,event):
        self.croix1 = self.create_line(event.x-10, event.y, event.x+10, event.y, fill="green",width=3)
        self.croix2 = self.create_line(event.x, event.y-10, event.x, event.y+10, fill="green",width=3)
        
    def deleteCroix(self):
        self.delete(self.croix1)
        self.delete(self.croix2)
        
        

