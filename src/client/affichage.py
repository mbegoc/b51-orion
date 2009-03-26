from Tkinter import *


###this should be part of Controler
#import xmlrpclib
#
#server='http://chryana.bounceme.net:6900'
#talkServer = xmlrpclib.ServerProxy(server) 

class Affichage:
    def __init__(self):
        #self.parent=parent
        self.root=Tk()
        self.root.title("Master of Orion")
        self.largeur=500
        self.hauteur=600

        self.canevas=Canvas(self.root,width=self.largeur, height=self.hauteur, bg="black")

        self.canevas.bind("<Button-1>", self.sendPosition)

        self.canevas.pack(side=TOP)

        ###code pour ajouter les menus
        #menu = Menu(self.root)
        #self.root.config(menu = menu)
        #PrincipalMenu = Menu(menu)
        #menu.add_cascade(label="Menu", command=)

        ########to delete
        planete=self.canevas.create_oval(100, 100, 105, 105, fill="white")

        self.root.mainloop()




    def sendPosition(self,event): #envoie la coordonnee de la souris au controleur
        #parent.sPosition(event.x,event.y)
        print event.x
        print event.y




        


allo=Affichage()




