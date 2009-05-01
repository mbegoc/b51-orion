from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import pickle
import datetime
import random
from modele.Systeme import Systeme
from modele.Univers import Univers
from modele.Joueur import Joueur
from modele.Vaisseau import Vaisseau
from modele.Chat import Chat

# Creer un serveur
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=SimpleXMLRPCRequestHandler)


# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class ControlleurServeur(object):
    def __init__(self):
        self.univers = Univers()
        self.creerSystemes()

        self.chat=Chat()

        #Attention: TESTS A REGARDER POUR AJOUTER QQCH DE SIMILAIRE DANS CONTROLLEUR_CLIENT!!!!!!!
        #Attention: POUR TESTER ENLEVER SEULEMENT LES COMMENTAIRES QUI SONT 
        #           AU DEBUT DE LIGNE (PAS DE <<Tabs>>) AVEC: << Source->Toggle comment >>
         
        
#        self.ConnecterJoueur("Eliana")
#        self.ConnecterJoueur("Eduardo")
#        self.ConnecterJoueur("Eliana")


        #Attenttion: ici Eliana cree un vaisseau dans (20,30) et elle l'envoie au serveur
#        vaisseauTest=Vaisseau(20,30)
#        self.univers.joueurs["Eliana"].vaisseaux.append(vaisseauTest)
#        reponse= self.MiseAJourVaisseaux("Eliana", pickle.dumps(self.univers.joueurs["Eliana"].vaisseaux))
#        print reponse


        #Attention: ici Eliana fait une requete mais il y a rien a "charger"
#        repServeur=self.requeteClient("Eliana")
#        print "Message a Eliana: ",
#        if(repServeur=="rien"):
#            print repServeur

     
        #Attention: ici Eduardo fait une requete, il doit afficher le vaisseau a Eliana dans (20,30)
#        repServeur=self.requeteClient("Eduardo")
#        print "Message a Eduardo: ",
#        if(repServeur=="rien"):
#            print repServeur
#        else:
#            self.univers.joueurs["Eduardo"].message=pickle.loads(repServeur)
#            message1 = self.univers.joueurs["Eduardo"].message.pop()
#            print message1[0],
#            print message1[1],
#            tempVaisseaux= message1[2]
#            print tempVaisseaux[0].x,
#            print tempVaisseaux[0].y
        
        
    def creerSystemes(self):
        s=0
        while s<10:  
            x=random.randint(0,50)*10 
            y=random.randint(0,60)*10
            if (s>1 and self.univers.validePositionSysteme(x,y)==1):
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

    def ConnecterJoueur(self, nom):         
        print "Ajoutant joueur: ",
        if(nom in self.univers.joueurs):
            tempReponse="Joueur existant"
            print tempReponse
        else:
            self.univers.ajouterJoueur(nom, self.chat.nbrMessage)
            tempReponse=pickle.dumps(self.univers)
            print "OK"
        return tempReponse
        
    def MiseAJourVaisseaux(self,nom,messVaisseaux):
        self.univers.joueurs[nom].vaisseaux=pickle.loads(messVaisseaux)
        self.MiseAJourMessage(nom,"vai", self.univers.joueurs[nom].vaisseaux)
        print "Mise a jour des vaisseaux: "
        return "ok"
             
    def MiseAJourMessage(self, nom, codMess, obj):
        for s in self.univers.joueurs:
            if(s <> nom):
                self.univers.joueurs[s].message.append((nom, codMess, obj))
                
    def requeteClient(self, nom):
        print "Dans requeteClient......"
        if(self.univers.joueurs[nom].message):
            return pickle.dumps(self.univers.joueurs[nom].message) 
        else:
            return "rien"


##################################
#chat

#debut du fichier


    def distributionMessageChat(self, nick, message):
        self.chat.distributionMessageChat(nick, message)
        return 0

    def receptionMessageChat(self, nick):
        if self.chat.nbrMessage > self.univers.joueurs[nick].chatnbrMessage:
            self.reponse = self.chat.receptionMessageChat(self.univers.joueurs[nick].chatnbrMessage)#stocke reponse
            self.univers.joueurs[nick].chatnbrMessage = self.univers.joueurs[nick].chatnbrMessage + 1#incremente message joueur
            return self.reponse
        else:
            return ["nobody","said nothing"]






#fin chat
#################################
#fermer serveur

    def shutdown(self):
        leChat.terminer()

#fin fermer serveur
################################




server.register_instance(ControlleurServeur())

# Demarrer la boucle du serveur
print "OK, serveur demarre"
print ""
print ""
server.serve_forever()
print "OK, serveur arrete"


    #IMPORTANT:
    #    * Ne pas accepter deux fois le meme nom dans ConnecterJoueur. OK!!!
    #    * Effacer messages:
    #            - Quand ils sont lues.
    #            - Quand ils sont "repetes".
    
            
            
            
            
