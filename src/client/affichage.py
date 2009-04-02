from Tkinter import *


###this should be part of Controler
#import xmlrpclib
#
#server='http://chryana.bounceme.net:6900'
#talkServer = xmlrpclib.ServerProxy(server) 



#le canevas principal du jeu. variable globale pour l'instant en attendant que le jeu soit davantage developpe.

class ecranGalaxie:
    def __init__(self):
        self.root=Tk()
        self.root.title("Master of Orion")

        self.largeur=500
        self.hauteur=600

        lecanevas=Canvas(self.root,width=self.largeur, height=self.hauteur, bg="black")#fix this
        allo=Dessin(lecanevas)
        self.root.mainloop()


class Dessin:
    def __init__(self, canevas):
        #self.parent=parent



        canevas.bind("<Button-1>", self.sendPosition)


        canevas.pack(side=TOP)

        ###code pour ajouter les menus
        #menu = Menu(self.root)
        #self.root.config(menu = menu)
        #PrincipalMenu = Menu(menu)
        #menu.add_cascade(label="Menu", command=)

        ########to delete
        ##section affichage d'elements avec un element statique pour le moment. eventuellement, recevra une liste d'objets a afficher a l'ecran.
        planete=canevas.create_oval(100, 100, 105, 105, fill="white")

        


    def sendPosition(self,event): #envoie la coordonnee de la souris au controleur
        #parent.sPosition(event.x,event.y)
        print event.x
        print event.y

x=ecranGalaxie()





