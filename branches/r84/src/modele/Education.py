from modele.Ressource import Ressource
import threading

class Education (Ressource):
    def __init__(self, niveau="Ecole"):
        Ressource.__init__(self)
        self.niveau = niveau
        self.isFini = true
        self.joueur = joueur
        self.infraestructure =Infraestructure ("Education")
                  
    def developEducation (self):
        if self.niveau=="Ecole":
            self.credit=0
            self.connaissance=1
            calculEducation()
            evolucioneEducation()
        if self.niveau=="Cegep":
            self.credit=2
            self.connaissance=4
            calculEducation()
            evolucioneEducation()
        if self.niveau=="Universite":
            self.credit=4
            self.connaissance=16
            calculEducation()
    def calculEducation (self):
        self.infraestructure.modificateurRessouces=self.credit
        self.infraestructure.ressourcesEntretien.connaissance = self.connaissance
 
    def evolutionerEducation(self):
        if(self.isFini):
            self.isFini=false 
            if self.niveau=="Ecole":
                self.niveau="Cegep"
                self.isFini=true
                ObjTimer=threading.Timer(600.0,EvolutionerEducation)
                ObjTimer.start()     
            if self.niveau=="Cegep":
                self.niveau="Universite"
                
                 

        
            
            
        