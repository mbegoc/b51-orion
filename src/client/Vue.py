'''
Created on 2009-04-02

@author: Michel
'''

from Tkinter import *

class Vue(object):
    def __init__(self):
        self.root = Tk()
        
        self.menuBas = MenuBas(self.root)
        self.menuBas.grid(column=0, row=2)
        
        self.menuCote = MenuCote(self.root)
        self.menuCote.grid(column=2, row=0)
        
        self.ssCanvas = SsCanvas(self.root)
        self.ssCanvas.grid(column=0, row=0)
    
        self.scrollY = Scrollbar(self.root, orient=VERTICAL, command=self.ssCanvas.yview)
        self.scrollY.grid(row=0, column=1, sticky=N+S)
    
        self.scrollX = Scrollbar(self.root, orient=HORIZONTAL, command=self.ssCanvas.xview)
        self.scrollX.grid ( row=1, column=0, sticky=E+W )
    
        self.ssCanvas["xscrollcommand"] = self.scrollX.set
        self.ssCanvas["yscrollcommand"] = self.scrollY.set
            
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
        Canvas.__init__(self, root, width=1000, height=600, background="#000000", scrollregion=(0, 0, 2000, 2000))
        self.create_line(0, 0, 2000, 2000, fill="#ffffff")
        self.create_line(2000, 0, 0, 2000, fill="#ffffff")

        
if __name__ == "__main__":
    vue = Vue()