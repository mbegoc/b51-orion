'''
Created on 2009-04-02

@author: Michel
'''

from client.Canvas import ZoneDeJeu
from Tkinter import *
import random

class Vue(object):
    def __init__(self, parent):
        self.root = Tk()
        self.root.title("Galax")
        self.parent = parent
        
        self.rouge = "#f00"
        self.vert = "#0f0"
        self.bleu = "#00f"
        self.cyan = "#0ff"
        self.jaune = "#ff0"
        self.brun = "#950"
        self.orange = "#da0"
        self.blanc = "#fff"
        self.gris = "#778"
        self.mauve = "#90f"
        
        
        self.zoneJeu = ZoneDeJeu(self)
        self.zoneJeu.grid(column=0, row=0)
        
        self.menuCote = MenuCote(self)
        self.menuCote.grid(column=2, row=0)
        
        self.chat = Chat(self)
        self.chat.grid(column=0, row=2)

        self.menuBas = MenuBas(self)
        self.menuBas.grid(column=0, row=3)
    
        self.scrollY = Scrollbar(self.root, orient=VERTICAL, command=self.zoneJeu.yview)
        self.scrollY.grid(row=0, column=1, sticky=N+S)
    
        self.scrollX = Scrollbar(self.root, orient=HORIZONTAL, command=self.zoneJeu.xview)
        self.scrollX.grid ( row=1, column=0, sticky=E+W )
    
        self.zoneJeu["xscrollcommand"] = self.scrollX.set
        self.zoneJeu["yscrollcommand"] = self.scrollY.set

        if __name__ == "__main__":
            self.root.mainloop()
    
class MenuBas(Frame):
    def __init__(self, parent):
        #appel au constructeur de la super classe
        Frame.__init__(self, parent.root)
        #on garde une reference vers la classe parent
        self.parent = parent

        self.nom = Label(self, text="Menu du bas")
        self.bouton1 = Button(self, text="Bouton 1")
        self.bouton2 = Button(self, text="Bouton 2")
        self.bouton3 = Button(self, text="Bouton 3")
        self.nom.pack(side=LEFT)# test du chat
        self.bouton1.pack(side=LEFT)
        self.bouton2.pack(side=LEFT)
        self.bouton3.pack(side=LEFT)

class Chat(Frame):
    def __init__(self, parent):
        #appel au constructeur de la super classe
        Frame.__init__(self, parent.root)
        #on garde une reference vers la classe parent
        self.parent = parent
        
        #preparation du chat
        self.message=Entry(self, width=132)
        '''j'aurais aime utilise la largeur de la zone de jeu et adapte automatiquement le chat a la meme taille,
        mais le probleme est que la dimension de ce %?*(?&* d'objet Text prend des dimensions en CARACTERES
        il me semble que ce n'est meme pas une unite, alors je sais pas comment on peut dimensionner un composant avec ca :(
        et je crois que je n'ai aucun moyen de connaitre la largeur d'un caractere donc... '''
        #test = self.parent.zoneJeu["width"]
        
        self.affichage=Text(self, width=138, height=5, wrap=WORD, state=DISABLED)
        self.envoi=Button(self,text="Envoi",command=self.sendMessage)# test du chat
        self.affichage.tag_configure("brun", foreground=self.parent.brun)
        self.affichage.tag_configure("jaune", foreground=self.parent.jaune)
        self.affichage.tag_configure("rouge", foreground=self.parent.rouge)
        self.affichage.tag_configure("bleu", foreground=self.parent.bleu)
        self.affichage.tag_configure("cyan", foreground=self.parent.cyan)
        self.affichage.tag_configure("orange", foreground=self.parent.orange)
        self.affichage.tag_configure("blanc", foreground=self.parent.blanc)
        self.affichage.tag_configure("gris", foreground=self.parent.gris)
        self.affichage.tag_configure("vert", foreground=self.parent.vert)
        self.affichage.tag_configure("mauve", foreground=self.parent.mauve)
        
        self.message.bind("<KeyRelease-Return>", self.sendMessage)
        
        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.affichage.yview)
        self.affichage["yscrollcommand"] = self.scrollY.set
        
        self.affichage.grid(column=0, row=0, columnspan=3)
        self.scrollY.grid(row=0, column=3, sticky=N+S)
        self.message.grid(column=0, row=1, columnspan=2)# test du chat
        self.envoi.grid(column=2,row=1, columnspan=2)# test du chat
        
    def sendMessage(self, event=None):
        self.parent.parent.chat.addMessage(self.message.get())
	self.parent.parent.chat.currentMessage()
        self.message.delete(0, END)
        
    def affiche(self, message, couleur=None):
        '''Cette maniere de faire pour bloquer la modification de l'affichage ne me plait pas, mais c'est la seule que j'ai trouve:
        normalement, il suffit de seter l'etat du text a DISABLE et l'utilisateur ne peut plus le modifier, par contre la doc dit qu'on peut
        le modifier par programmation. Sauf que ca ne marche pas.
        Je suis donc oblige de retablir l'etat normal le temps de la mise a jour.
        En plus, la constante DISABLE ne fonctionne que dans le contexte du constructeur, ce qui fait que ca ne marche pas dans le code 
        ci-dessous, et je suis donc oblige de sauver la valeur de l'option pour pouvoir la reattribuer ensuite.'''
        disable = self.affichage["state"]
        self.affichage["state"] = NORMAL
        
        self.affichage.insert("0.0", message+"\n")
        if couleur != None:
            self.affichage.tag_add(couleur, "0.0", END)
        
        self.affichage["state"] = disable

class MenuCote(Frame):
    def __init__(self, parent):
        #appel au constructeur de la super classe
        Frame.__init__(self, parent.root)
        #on garde une reference vers la classe parent
        self.parent = parent

        self.bouton1 = Button(self, text="Dessiner jeu")
        self.bouton1.bind("<Button-1>", self.representerJeu)
        self.bouton2 = Button(self, text="Delete")
        self.bouton2.bind("<Button-1>", self.deleteJeu)
        self.bouton3 = Button(self, text="Move")
        self.bouton3.bind("<Button-1>", self.moveJeu)
        self.bouton4 = Button(self, text="Systeme ;)")
        self.bouton4.bind("<Button-1>", self.systeme)
        self.nom = Label(self, text="Menu de cote")
        self.nom.pack()
        self.bouton1.pack()
        self.bouton2.pack()
        self.bouton3.pack()
        self.bouton4.pack()

    def representerJeu(self, evt):
        self.parent.zoneJeu.representerJeu()
        
    def deleteJeu(self, evt):
        self.parent.zoneJeu.deleteJeu()
    
    def moveJeu(self, evt):
        self.parent.zoneJeu.moveJeu()
        
    def systeme(self, evt):
        r = random.Random()
        self.parent.zoneJeu.dessinerImage("systeme2", r.randint(0, 2000), r.randint(0, 2000))
