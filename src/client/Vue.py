'''
Created on 2009-04-02

@author: Michel
'''

from Tkinter import *
import random
import glob, os
from modele.Vaisseau import Vaisseau

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
        self.grille= "#799990"
        
        
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
        
        #tests -- a supprimer des que les controlleurs sont fonctionnels
        for i in range(200):
            r = random.Random()
            self.zoneJeu.dessinerImage("systeme3", r.randint(0, 2000), r.randint(0, 2000), "test")
        self.zoneJeu.nouveauVaisseauMilitaire(Vaisseau(200, 200))
        self.zoneJeu.nouveauVaisseauMilitaire(Vaisseau(100, 180))
        self.zoneJeu.nouveauVaisseauCivil(Vaisseau(210, 230))
        self.zoneJeu.nouveauVaisseauCivil(Vaisseau(80, 120))
        self.zoneJeu.nouvelleSonde(600, 500)
        
    
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
        self.parent.parent.chat.sendMessage(self.message.get())
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
        self.parent.zoneJeu.dessinerImage("systeme2", r.randint(0, 2000), r.randint(0, 2000), "test")



class ZoneDeJeu(Canvas):
    def __init__(self, parent):
        '''definition des differents parametres de l'affichage 
        definitions faites avant l'appel au constructeur car le constructeur a besoin de certaines de ces valeurs'''
        self.largeurVue = 1000
        self.hauteurVue = 600
        self.largeurMonde = 2000
        self.hauteurMonde = 2000
        self.largeurGrille = 200
        self.baseUnites = 5
        self.itemSelectionne = None

        #appel au constructeur de la super classe
        Canvas.__init__(self, parent.root, width=self.largeurVue, height=self.hauteurVue, background="#000000", scrollregion=(0, 0, self.largeurMonde, self.hauteurMonde))
        
        #on garde une reference vers la classe parent
        self.parent = parent
        
        # rond autour de l'entite selectionne
        self.rondSelection = None 
        # x qui represente le cible de deplacement ou d'attaque besoin de 2 lignes
        self.croix1 = None 
        self.croix2 = None
        
        #initialisation des images disponibles
        self.images = {}
        ZoneDeJeu.__genererImages__(self)

        #tracage du cadrillage style "tactique"
        for i in range(0, self.largeurMonde, self.largeurGrille):
            self.create_line(0, i, self.largeurMonde, i, fill=self.parent.grille)
        for i in range(0, self.hauteurMonde, self.largeurGrille):
            self.create_line(i, 0, i, self.largeurMonde, fill=self.parent.grille)

        #binds des evenements
        self.bind("<Button-1>", self.gestionClic) #envoie l'objet event au controlleur
        self.bind("<Button-3>", self.parent.parent.ClickEvent) #envoie l'objet event au controlleur

    #representer l'ensemble des sytemes initiaux
    def initialiserSystemes(self, systemes):
        for systeme in systemes:
            self.dessinerImage("systeme2", systeme.x, systeme.y, systeme.nom)
        
    def detruireSysteme(self, systeme):
        self.delete("systeme.nom")
        self.dessinerImage("nebuleuse", systeme.x, systeme.y, systeme.nom)
        
    def nouveauVaisseauMilitaire(self, vaisseau):
        x = vaisseau.x
        y = vaisseau.y
        l = self.baseUnites*2 #largeur des unites
        self.create_polygon(x+self.baseUnites, y, x+l, y+l, x, y+l, fill=self.parent.rouge, tags=vaisseau.nom)
        
    def nouveauVaisseauCivil(self, vaisseau):
        x = vaisseau.x
        y = vaisseau.y
        l = self.baseUnites*2 #largeur des unites
        self.create_rectangle(x, y, x+l, y+l, fill=self.parent.vert, tags=vaisseau.nom)
        self.tag_bind(vaisseau.nom, "<Button-1>", self.testTagBind)
        
    def nouvelleSonde(self, x, y):
        l = self.baseUnites #largeur des unites
        self.create_oval(x, y, x+l, y+l, fill=self.parent.bleu)
        
    def deplacerVaisseau(self, vaisseau):
        self.coords(vaisseau.nom, vaisseau.x-self.baseUnites, vaisseau.y-self.baseUnites, vaisseau.x+self.baseUnites, vaisseau.y+self.baseUnites)
        
    def gestionClic(self, event):
        xy = self.calculerPositionReelle((event.x,event.y))
        x = xy[0]
        y = xy[1]
                
        #deselection de l'item acutellement selectionne
        if self.itemSelectionne != None:
            self.itemconfigure(self.itemSelectionne, outline="")
        self.itemSelectionne = None
        
        #selection d'un ou plusieurs objets
        objetsCliques = self.find_overlapping(x-self.baseUnites, y-self.baseUnites, x+self.baseUnites, y+self.baseUnites)
        
        #on commence par creer une liste avec seulement les objets qui nous interessent
        objets = []
        for objet in objetsCliques:
            if self.type(objet) != "line":
                objets.append(objet)
        
        if len(objets) == 1:
            type = self.type(objets[0])
            '''on recupere le premier tag sur l'objet - normalement il doit y en avoir qu'un. Si il y en a plusieurs, il va y avoir des bugs ici
            A priori, la seule solution qu'il y aurait ce serait de connaitre tous les autres tags que celui qui identifie l'objet et de les tester'''
            tag = self.gettags(objets[0])
            print tag[0]# pour le moment on print le nom de l'objet, apres il va falloir l'envoyer au controlleur client pour qu'il connaisse l'objet selectionne
            if type == "polygon" or type == "oval" or type == "rectangle":
                print "forme"
                self.itemconfigure(objets[0], outline=self.parent.blanc)
                self.itemSelectionne = objets[0]
            elif type == "image":
                position = self.coords(objets[0])
                self.itemSelectionne = self.create_oval(position[0]-self.baseUnites*2, position[1]-self.baseUnites*2, position[0]+self.baseUnites*2, position[1]+self.baseUnites*2, outline=self.parent.blanc)
        elif len(objets) > 1:
            self.menu = Menu(self, tearoff=0)
            #ici il faut recuperer la liste des tags objets et demander la liste des objets au controlleur
            self.menu.add_command(label="Type", command=self.getType)
            self.x,self.y = event.x,event.y
            self.menu.post(event.x_root, event.y_root)
        
    def getType(self):
        self.item=self.find_closest(self.x,self.y,halo=5)
        print self.type(self.item)

    '''ce calcule est necessaire, car l'event contient la position du clic sur la fenetre, pas sur le canvas. 
    Il faut donc convertir cette position en fonction de la valeur de 'scroll' du canvas''' 
    def calculerPositionReelle(self, xy):
        x = self.xview()[0]*self.largeurMonde+xy[0]
        y = self.yview()[0]*self.hauteurMonde+xy[1]
        return (x,y)
        

   
    def drawCroix(self,event):
        xy = self.calculerPositionReelle((event.x,event.y))
        x = xy[0]
        y = xy[1]
        self.croix1 = self.create_line(x-10, y, x+10, y, fill="green",width=3)
        self.croix2 = self.create_line(x, y-10, x, y+10, fill="green",width=3)
        
    def deleteCroix(self):
        self.delete(self.croix1)
        self.delete(self.croix2)

        
    '''ATTENTION: cette fonction doit imperativement etre appelee a travers la classe de l'objet, par par l'objet lui meme (ZoneDeJeu.__genererImages__(objet) )
    Je ne sais pas pourquoi, mais si l'image est generee dans l'objet sur lequel elle va etre affichee, ca ne marche pas. Il faut donc appeler cette methode
    sur la classe et passer en parametre l'instance d'un ZoneDeJeu dans lequel la liste d'images sera cree'''
    #genere un dictionnaire des images contenues dans le repertoire images. La clef utilisee comme entree du dictionnaire est le nom de base du fichier (sans extension)
    def __genererImages__(instance):
        for image in glob.glob("images/*"):
            photo = PhotoImage(file=image)
            key = os.path.splitext(os.path.split(image)[1])[0]
            instance.images[key] = photo
        
    #cette fonction ne sert qu'a simplifier le dessin des images
    def dessinerImage(self, nom, x, y, tag):
        if nom in self.images:
            self.create_image(x, y, image=self.images[nom], tags=tag)
            return 0
        else:
            return 1
    
    #test de bind evenement sur objet du canvas
    def testTagBind(self, event):
        print "tagBind"
