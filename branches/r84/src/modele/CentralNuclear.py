from modele.Ressource import Ressource
import threading

class CentralNuclear (Ressource):
    def __init__(self, niveau="basic"):
        Ressource.__init__(self)
        self.niveau = niveau
        self.isFini = true
        self.infraestructure =Infraestructure ("CentralNuclear")
                  
    def developCentralNuclear (self):
        if self.niveau=="basic":
            self.credit=0
            self.energie=1
            calculCentral()
            evolucioneCentral()
        if self.niveau=="mediane":
            self.credit=2
            self.energie=4
            calculCentral()
            evolucioneCentral()
        if self.niveau=="avance":
            self.credit=4
            self.energie=16
            calculCentral()
    def calculCentralNuclear (self):
        self.infraestructure.modificateurRessouces=self.credit
        self.infraestructure.ressourcesEntretien.energie = self.energie
 
    def evolutionerCentralNuclear(self):
        if(self.isFini):
            self.isFini=false 
            if self.niveau=="basic":
                self.niveau="mediane"
                self.isFini=true
                ObjTimer=threading.Timer(600.0,EvolutionerCentralNuclear)
                ObjTimer.start()     
            if self.niveau=="mediane":
                self.niveau="avance"