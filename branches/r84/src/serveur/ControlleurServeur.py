from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import pickle
import datetime
import random
from modele.Systeme import Systeme
from modele.Univers import Univers
from modele.Joueur import Joueur

#seulement pour tester
from modele.Vaisseau import Vaisseau


# Creer un serveur
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=SimpleXMLRPCRequestHandler)


# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class ControlleurServeur(object):
    def __init__(self):
        self.univers = Univers()
        self.creerSystemes()
        

        # seulement commentaires.....
#        self.ConnecterJoueur("Eliana")
#        self.ConnecterJoueur("Eduardo")
#        vaisseauTest=Vaisseau(20,20)
#        self.univers.joueurs["Eliana"].vaisseaux.append(vaisseauTest)
#        self.MiseAJourVaisseaux("Eliana", pickle.dumps(self.univers.joueurs["Eliana"].vaisseaux))
#     
#        tempMessage=self.requeteClient("Eduardo")
#        print tempMessage
#        self.univers.joueurs["Eduardo"].message=pickle.loads(tempMessage)
#        message1 = self.univers.joueurs["Eduardo"].message.pop()
#        print "Message a Eduardo: "
#        print message1[0]
#        print message1[1]
#        print message1[2]         
#        listeVaiseauxTemp = pickle.loads(message1[2])
#        print listeVaiseauxTemp        
        
        
    def creerSystemes(self):
        s=0
        while s<10:  
            x=random.randint(0,50)*10 
            y=random.randint(0,60)*10
            if (s>1 and self.univers.validePositionSysteme(x,y)==1):
                print s
                print "systeme existant!!!!"
            else:
                s=s+1
                print "nouveau systeme"
                systeme=Systeme(x,y)
                self.univers.ajouterSysteme(systeme)
        
        print "systCrees!!!"
        for i in range(len(self.univers.systemes)):
            print i,
            print "..[i].x=",
            print self.univers.systemes[i].x
            print i,
            print "..[i].y=",
            print self.univers.systemes[i].y
            print "****"        

    def ConnecterJoueur(self, nom):         #Attention: il faut verifier noms differents
#        if(not self.univers.joueurs):
        print "Ajoutant joueur"
        self.univers.ajouterJoueur(nom)
        return pickle.dumps(self.univers)
        
    def MiseAJourVaisseaux(self,nom,messVaisseaux):
        self.univers.joueurs[nom].vaisseaux=pickle.loads(messVaisseaux)
        self.MiseAJourMessage(nom,"vai", messVaisseaux)
        print "Mise a jour des vaisseaux: "
        print messVaisseaux
        return "ok"
             
    def MiseAJourMessage(self, nom, codMess, messObj):
        for s in self.univers.joueurs:
            if(s <> nom):
                self.univers.joueurs[s].message.append((nom, codMess, messObj))
                
    def requeteClient(self, nom):
        print "Dans requeteClient......"
        if(self.univers.joueurs[nom].message):
            return pickle.dumps(self.univers.joueurs[nom].message) 
        else:
            return "rien"



server.register_instance(ControlleurServeur())

# Demarrer la boucle du serveur
print "OK, serveur demarrer"
server.serve_forever()
print "OK, serveur arreter"
