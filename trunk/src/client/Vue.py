'''
Created on 2009-04-02

@author: Michel
'''

from client.canvas import ZoneDeJeu
from Tkinter import *

class Vue(object):
    def __init__(self):
        self.root = Tk()
        self.root.title = "Galax"
        
        self.menuBas = MenuBas(self)
        self.menuBas.grid(column=0, row=2)
        
        self.menuCote = MenuCote(self)
        self.menuCote.grid(column=2, row=0)
        
        self.zoneJeu = ZoneDeJeu(self)
        self.zoneJeu.grid(column=0, row=0)
    
        self.scrollY = Scrollbar(self.root, orient=VERTICAL, command=self.zoneJeu.yview)
        self.scrollY.grid(row=0, column=1, sticky=N+S)
    
        self.scrollX = Scrollbar(self.root, orient=HORIZONTAL, command=self.zoneJeu.xview)
        self.scrollX.grid ( row=1, column=0, sticky=E+W )
    
        self.zoneJeu["xscrollcommand"] = self.scrollX.set
        self.zoneJeu["yscrollcommand"] = self.scrollY.set

        if __name__ == "__main__":
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

if __name__ == "__main__":
    vue = Vue()