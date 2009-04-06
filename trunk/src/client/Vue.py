'''
Created on 2009-04-02

@author: Michel
'''

from Tkinter import *
from PIL import Image, ImageTk
import glob, os

class Vue(object):
    def __init__(self):
        self.root = Tk()
        self.root.title = "Galax"
        
        self.menuBas = MenuBas(self)
        self.menuBas.grid(column=0, row=2)
        
        self.menuCote = MenuCote(self)
        self.menuCote.grid(column=2, row=0)
        
        self.ssCanvas = SsCanvas(self)
        self.ssCanvas.grid(column=0, row=0)
    
        self.scrollY = Scrollbar(self.root, orient=VERTICAL, command=self.ssCanvas.yview)
        self.scrollY.grid(row=0, column=1, sticky=N+S)
    
        self.scrollX = Scrollbar(self.root, orient=HORIZONTAL, command=self.ssCanvas.xview)
        self.scrollX.grid ( row=1, column=0, sticky=E+W )
    
        self.ssCanvas["xscrollcommand"] = self.scrollX.set
        self.ssCanvas["yscrollcommand"] = self.scrollY.set

        self.root.mainloop()
    
class MenuBas(Frame):
    def __init__(self, mere):
        #appel au constructeur de la super classe
        Frame.__init__(self, mere.root)
        #on garde une reference vers la classe mere
        self.mere = mere

        self.nom = Label(self, text="Menu du bas")
        self.bouton1 = Button(self, text="Bouton 1")
        self.bouton2 = Button(self, text="Bouton 2")
        self.bouton3 = Button(self, text="Bouton 3")
        self.nom.pack(side=LEFT)
        self.bouton1.pack(side=LEFT)
        self.bouton2.pack(side=LEFT)
        self.bouton3.pack(side=LEFT)

class MenuCote(Frame):
    def __init__(self, mere):
        #appel au constructeur de la super classe
        Frame.__init__(self, mere.root)
        #on garde une reference vers la classe mere
        self.mere = mere

        self.bouton1 = Button(self, text="Dessiner jeu")
        self.bouton1.bind("<Button-1>", self.representerJeu)
        self.bouton2 = Button(self, text="Delete")
        self.bouton2.bind("<Button-1>", self.deleteJeu)
        self.bouton3 = Button(self, text="Move")
        self.bouton3.bind("<Button-1>", self.moveJeu)
        self.nom = Label(self, text="Menu de cote")
        self.nom.pack()
        self.bouton1.pack()
        self.bouton2.pack()
        self.bouton3.pack()

    def representerJeu(self, evt):
        self.mere.ssCanvas.representerJeu()
        
    def deleteJeu(self, evt):
        self.mere.ssCanvas.deleteJeu()
    
    def moveJeu(self, evt):
        self.mere.ssCanvas.moveJeu()
        
class SsCanvas(Canvas):
    def __init__(self, mere):
        #appel au constructeur de la super classe
        Canvas.__init__(self, mere.root, width=1000, height=600, background="#000000", scrollregion=(0, 0, 2000, 2000))
        #on garde une reference vers la classe mere
        self.mere = mere
        
        #initialisation des images disponibles
        self.images = {}
        SsCanvas.__genererImages__(self)

        self.create_line(0, 0, 2000, 2000, fill="#ffffff")
        self.create_line(2000, 0, 0, 2000, fill="#ffffff")

    #cette fonction ne sert qu'a 
    def dessinerImage(self, nom, x, y):
        if nom in self.images:
            self.create_image(x, y, image=self.images[nom], tags=nom)
            return 1
        else:
            return 0

    '''ATTENTION: cette fonction doit imperativement etre appelee a travers la classe de l'objet, par par l'objet lui meme (SsCanvas.__genererImages__(objet) )
    Je ne sais pas pourquoi, mais si l'image est generee dans l'objet sur lequel elle va etre affichee, ca ne marche pas. Il faut donc appeler cette methode
    sur la classe et passer en parametre l'instance d'un SsCanvas dans lequel la liste d'images sera cree'''
    #genere un dictionnaire des images contenues dans le repertoire images. La clef utilisee comme entree du dictionnaire est le nom de base du fichier (sans extension)
    def __genererImages__(instance):
        for file in glob.glob("images/*"):
            image = Image.open(file)
            photo = ImageTk.PhotoImage(image)
            key = os.path.splitext(os.path.split(file)[1])[0]
            instance.images[key] = photo

    def representerJeu(self):
        self.dessinerImage("abasourdi", 115, 100)
        self.dessinerImage("bise", 65, 100)
        self.dessinerImage("cligne", 50, 170)
        self.dessinerImage("etonne", 70, 190)
        self.dessinerImage("prof", 90, 190)
        self.dessinerImage("ricane", 110, 190)
        self.dessinerImage("yeuxLeves", 130, 170)
        
    def deleteJeu(self):
        self.delete("abasourdi")
        self.delete("bise")
        self.delete("cligne")
        self.delete("etonne")
        self.delete("prof")
        self.delete("ricane")
        self.delete("yeuxLeves")
        
    def moveJeu(self):
        self.move("abasourdi", 5, 5)
        self.move("bise", 5, 5)
        self.move("cligne", 5, 5)
        self.move("etonne", 5, 5)
        self.move("prof", 5, 5)
        self.move("ricane", 5, 5)
        self.move("yeuxLeves", 5, 5)
        
if __name__ == "__main__":
    vue = Vue()