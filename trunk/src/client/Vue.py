'''
Created on 2009-04-02

@author: Michel
'''

from Tkinter import *

class Vue(object):
    def __init__(self):
        self.root = Tk()
        
        self.menuBas = MenuBas(self.root)
        self.menuBas.grid(column=0, row=1)
        
        self.menuCote = MenuCote(self.root)
        self.menuCote.grid(column=1, row=0)
        
        self.ssCanvas = SsCanvas(self.root)
        self.ssCanvas.grid(column=0, row=0)
        
        self.root.mainloop()
    
class MenuBas(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.nom = Label(self, text="Menu du bas")
        self.bouton1 = Button(self, text="Bouton 1")
        self.bouton2 = Button(self, text="Bouton 2")
        self.bouton3 = Button(self, text="Bouton 3")
        self.nom.pack(side=LEFT)
        self.bouton1.pack(side=LEFT)
        self.bouton2.pack(side=LEFT)
        self.bouton3.pack(side=LEFT)
    
class MenuCote(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.bouton1 = Button(self, text="Bouton 1")
        self.bouton2 = Button(self, text="Bouton 2")
        self.bouton3 = Button(self, text="Bouton 3")
        self.nom = Label(self, text="Menu de cote")
        self.nom.pack()
        self.bouton1.pack()
        self.bouton2.pack()
        self.bouton3.pack()

class SsCanvas(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, root, width=200, height=200)
        self.create_line(0, 0, 200, 200)
        
if __name__ == "__main__":
    vue = Vue()