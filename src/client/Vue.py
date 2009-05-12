'''
Created on 2009-04-02

@author: Michel
'''

from Tkinter import *
import random
import glob, os
from modele.Vaisseau import Vaisseau
import tkMessageBox as MBox
from threading import Timer

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
        
        self.connexion = Connexion(self)
        self.connexion.pack()
            
    def demarrerJeu(self):
        self.connexion.pack_forget()

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
#        for i in range(200):
#            r = random.Random()
#            self.zoneJeu.dessinerImage("systeme3", r.randint(0, 2000), r.randint(0, 2000), "system"+str(i))
        
    
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
        self.envoi=Button(self,text="Envoi",command=self.distributionMessageChat)# test du chat
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
        
        self.message.bind("<KeyRelease-Return>", self.distributionMessageChat)
        
        self.scrollY = Scrollbar(self, orient=VERTICAL, command=self.affichage.yview)
        self.affichage["yscrollcommand"] = self.scrollY.set
        
        self.affichage.grid(column=0, row=0, columnspan=3)
        self.scrollY.grid(row=0, column=3, sticky=N+S)
        self.message.grid(column=0, row=1, columnspan=2)# test du chat
        self.envoi.grid(column=2,row=1, columnspan=2)# test du chat
        
    def distributionMessageChat(self, event=None):
        self.parent.parent.distributionMessageChat(self.message.get())
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
        vaisseau = Vaisseau(500, 500)
        vaisseau.nom = self.parent.zoneJeu.itemSelectionne
        self.parent.zoneJeu.deplacerVaisseau(vaisseau) 
        
        
    def systeme(self, evt):
        r = random.Random()
        self.parent.zoneJeu.dessinerImage("systeme2", r.randint(0, 2000), r.randint(0, 2000), "test")



class Connexion(Frame):
    def __init__(self, parent):
        #appel au constructeur de la super classe
        Frame.__init__(self, parent.root)

        #on garde une reference vers la classe parent
        self.parent = parent
        self.nom=Entry(self, width=50)
        self.nom.insert(0, "Default")
        self.ip=Entry(self, width=50)
        self.ip.insert(0, "localhost")
        self.lnom = Label(self, text="Joueur: ", )
        self.lip = Label(self, text="Serveur: ")
        self.envoi=Button(self,text="Envoi",command=self.connecter)
        
        self.lnom.grid(column=0, row=0)
        self.nom.grid(column=1, row=0)
        self.lip.grid(column=0, row=1)
        self.ip.grid(column=1, row=1)
        self.envoi.grid(column=1, row=2)

    def connecter(self):
        if self.nom.get() != "" and self.ip.get() != "":
            self.parent.parent.BoiteConnection(self.nom.get(), self.ip.get())
        else:
            MBox.showinfo(title="Saisie erronee", message="Toutes les informations demandees sont necessaires.")
            
    def erreurConnexion(self):
        MBox.showinfo(title="Erreur de connexion", message="Impossible de se connecter au serveur.")



class ZoneDeJeu(Canvas):
    def __init__(self, parent):
        '''definition des differents parametres de l'affichage 
        definitions faites avant l'appel au constructeur car le constructeur a besoin de certaines de ces valeurs'''
        self.largeurVue = 1000
        self.hauteurVue = 600
        self.largeurUnivers = 2000
        self.hauteurUnivers = 2000
        self.largeurGrille = 200
        self.baseUnites = 5
        self.itemSelectionne = None

        #appel au constructeur de la super classe
        Canvas.__init__(self, parent.root, width=self.largeurVue, height=self.hauteurVue, background="#000000", scrollregion=(0, 0, self.largeurUnivers, self.hauteurUnivers))
        
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
        for i in range(0, self.largeurUnivers, self.largeurGrille):
            self.create_line(0, i, self.largeurUnivers, i, fill=self.parent.grille)
        for i in range(0, self.hauteurUnivers, self.largeurGrille):
            self.create_line(i, 0, i, self.largeurUnivers, fill=self.parent.grille)

        #binds des evenements
        self.bind("<Button-1>", self.selectionner) #envoie l'objet event au controlleur
        self.bind("<Button-2>", self.creerVaisseau)
        self.bind("<Button-3>", self.cibler) #envoie l'objet event au controlleur

    #representer l'ensemble des sytemes initiaux
    def initialiserSystemes(self, systemes):
        i = 0
        for systeme in systemes:
            self.dessinerImage("systeme3", systeme.x, systeme.y, i)#systeme.nom)
            i=i+1
        
    def nouveauVaisseau(self, vaisseau):
        print "creation vaisseau", vaisseau.classe
        x = vaisseau.x
        y = vaisseau.y
        l = self.baseUnites #largeur des unites
        if(vaisseau.classe == "civil"):
            self.create_rectangle(x-l, y-l, x+l, y+l, fill=self.parent.vert, tags=vaisseau.id)
        elif(vaisseau.classe == "militaire"):
            self.create_polygon(x, y-l, x+l, y+l, x-l, y+l, fill=self.parent.rouge, tags=vaisseau.id)
        elif(vaisseau.classe == "sonde"):
            l = self.baseUnites #largeur des unites
            self.create_oval(x-l, y-l, x+l, y+l, fill=self.parent.bleu)
        #self.tag_bind(vaisseau.id, "<Button-1>", self.testTagBind)
        
    def deplacerVaisseau(self, vaisseau):
        x = vaisseau.x
        y = vaisseau.y
        l = self.baseUnites #largeur des unites
        if(vaisseau.classe == "militaire"):
            self.coords(vaisseau.id, x, y-l, x+l, y+l, x-l, y+l)
        else:
            l = self.baseUnites #largeur des unites
            self.coords(vaisseau.id, x-l, y-l, x+l, y+l)
            
    def existe(self, objet):
        objets = self.find_withtag(objet)
        return len(objets)
        
    def selectionner(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
                
        #deselection de l'item acutellement selectionne
        if self.itemSelectionne != None:
            self.itemconfigure(self.itemSelectionne, outline="")
        self.itemSelectionne = None
        
        self.parent.parent.objetSelectionne = selectionnerObjet(x, y)
            
    def creerVaisseau(self, event):
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        self.parent.parent.creerVaisseau(x, y)
    
    def cibler(self, event):
        self.deleteCroix()
        x = self.canvasx(event.x)
        y = self.canvasy(event.y)
        self.drawCroix(x, y)
        self.timer = Timer(1, self.deleteCroix)
        self.timer.start()
        self.parent.parent.TypeAction(x, y)
        self.parent.parent.objetCible = selectionnerObjet(x, y)

    def selectionnerObjet(self, x, y):
        #selection d'un ou plusieurs objets
        objetsCliques = self.find_overlapping(x-self.baseUnites, y-self.baseUnites, x+self.baseUnites, y+self.baseUnites)
        
        #on commence par creer une liste avec seulement les objets qui nous interessent
        objets = []
        for objet in objetsCliques:
            if self.type(objet) != "line":
                objets.append(objet)
        
        if len(objets) == 1:
            return objets[0]
        elif len(objets) > 1:
            print "Objets supperposes pas encore supprotees"
            '''self.menu = Menu(self, tearoff=0)
            #ici il faut recuperer la liste des tags objets et demander la liste des objets au controlleur
            for objet in objets:
                tag = self.gettags(objet)
                self.menu.add_command(label=tag[0], command=self.selectionnerObjetHandler(tag[0]))
            
            self.x,self.y = event.x,event.y
            self.menu.post(event.x_root, event.y_root)'''
        elif len(objets) == 0:
            return None      

    def selectionnerObjetHandler(self, tag):
        self.selectionnerObjet(tag)

    def selectionnerObjet(self, objet):
        type = self.type(objet)
        '''on recupere le premier tag sur l'objet - normalement il doit y en avoir qu'un. Si il y en a plusieurs, il va y avoir des bugs ici
        A priori, la seule solution qu'il y aurait ce serait de connaitre tous les autres tags que celui qui identifie l'objet et de les tester'''
        tag = self.gettags(objet)
        if type == "polygon" or type == "oval" or type == "rectangle":
            self.parent.parent.objetSelectionne = ("vaisseau", tag[0])
            self.itemconfigure(objet, outline=self.parent.blanc)
            self.itemSelectionne = objet
        elif type == "image":
            self.parent.parent.objetSelectionne = ("systeme", tag[0])
            position = self.coords(objet)
            self.itemSelectionne = self.create_oval(position[0]-self.baseUnites*2, position[1]-self.baseUnites*2, position[0]+self.baseUnites*2, position[1]+self.baseUnites*2, outline=self.parent.blanc)
   
    def drawCroix(self,x, y):
        self.croix1 = self.create_line(x-7, y, x+7, y, fill="green",width=2)
        self.croix2 = self.create_line(x, y-7, x, y+7, fill="green",width=2)
        
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
