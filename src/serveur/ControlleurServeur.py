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
        self.listeJoueurs=[]

        #Attention: TESTS A REGARDER POUR AJOUTER QQCH DE SIMILAIRE DANS CONTROLLEUR_CLIENT!!!!!!!
        #Attention: POUR TESTER ENLEVER SEULEMENT LES COMMENTAIRES QUI SONT 
        #           AU DEBUT DE LIGNE (PAS DE <<Tabs>>) AVEC: << Source->Toggle comment >>
        
#        self.ConnecterJoueur("Eliana")
#        self.ConnecterJoueur("Eduardo")
#        self.ConnecterJoueur("Eliana")
#        self.ConnecterJoueur("Carlos")
#
#        #Attenttion: ici Eliana cree un vaisseau dans (20,30) et elle l'envoie au serveur
#        #vaisseauTest1=Vaisseau(20,30,"vEliana1")
#        #vaisseauTest2=Vaisseau(5,7,"vEliana2")
#        self.univers.joueurs["Eliana"].ajouterVaisseau(20,30,"vEliana1")
#        self.univers.joueurs["Eliana"].ajouterVaisseau(5,7,"vEliana2")
#        reponse= self.MiseAJourVaisseaux("Eliana", pickle.dumps(self.univers.joueurs["Eliana"].vaisseaux))
#        print reponse
#        
#        #Attention: ici Eliana modifie la position des vaisseaux        
#        self.player=self.univers.joueurs["Eliana"]
#        for i in range(len(self.player.vaisseaux)):
#            self.player.getVaisseau(i+1).x=self.player.getVaisseau(i+1).x +1
#            self.player.getVaisseau(i+1).y=self.player.getVaisseau(i+1).y +1        
#            print self.player.getVaisseau(i+1).x,
#            print self.player.getVaisseau(i+1).y         
#        reponse= self.MiseAJourVaisseaux("Eliana", pickle.dumps(self.univers.joueurs["Eliana"].vaisseaux))
#        #print reponse
#
#        #Attention: ici Eliana fait une requete mais il y a rien a "charger"
#        repServeur=self.requeteClient("Eliana")
#        print "Message a Eliana: ",
#        if(repServeur=="rien"):
#            print repServeur
#     
#        #Attention: ici Eduardo fait 3 requetes, il doit afficher les vaisseau a Eliana deplaces
#        for i in range(0,3):
#            repServeur=self.requeteClient("Eduardo")
#            print i,
#            print "...Message a Eduardo: ",
#            if(repServeur=="rien"):
#                print repServeur
#            else:
#                self.univers.joueurs["Eduardo"].message=pickle.loads(repServeur)
#                while(self.univers.joueurs["Eduardo"].message):
#                    message1=self.univers.joueurs["Eduardo"].message.pop()
#                    print message1
##                    listeVaisseaux=pickle.loads(message1[2])
#                    listeVaisseaux=message1[2]                    
#                    for tempNomVai in listeVaisseaux:
#                        #print tempNomVai
#                        print listeVaisseaux[tempNomVai].x,
#                        print listeVaisseaux[tempNomVai].y
#                    
#        # Test checkNouveauxJoueurs
#        nouvelleListe=pickle.loads(self.checkNouveauxJoueurs(["Eliana","Eduardo"]))
#        for s in nouvelleListe:
#            print s
#            print s.id
                    
        
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
            self.univers.ajouterJoueur(nom)
            tempReponse=pickle.dumps(self.univers)
            print "OK"
        return tempReponse
        
    def MiseAJourVaisseaux(self,nom,messVaisseaux):
        self.univers.joueurs[nom].vaisseaux=pickle.loads(messVaisseaux)
        self.chercheMessagesAEffacer(nom,"vai")
        self.MiseAJourMessage(nom,"vai", self.univers.joueurs[nom].vaisseaux)
        print "Mise a jour des vaisseaux: "
        #print messVaisseaux
        return "ok"

    def chercheMessagesAEffacer(self, nom, codMess):
        for s in self.univers.joueurs:
            if(s <> nom):
                for tempMessage in self.univers.joueurs[s].message:
                    print "messageAEffacer???????????????",
                    print tempMessage
                    if tempMessage[0]==nom and tempMessage[1]=="vai":
                        self.univers.joueurs[s].message.remove(tempMessage)
             
    def MiseAJourMessage(self, nom, codMess, obj):
        for s in self.univers.joueurs:
            if(s <> nom):
                self.univers.joueurs[s].message.append([nom, codMess, obj])
                
    def checkNouveauxJoueurs(self, listeNomsJoueurs):
        print "Dans checkNouveauxJoueurs"
        #self.listeJoueurs=listeJoueurs
        for s in self.listeJoueurs:
            self.listeJoueurs.remove(s)
        for s in self.univers.joueurs:
            if (s not in listeNomsJoueurs):
                self.listeJoueurs.append(self.univers.joueurs[s])
        return pickle.dumps(self.listeJoueurs)

                    
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

    def receptionMessageChat(self, msgNbr):
        if msgNbr == -1: #demande no dernier message envoye
            self.reponse = self.chat.nbrMessage
        else: #demande un message precis
            self.reponse = self.chat.receptionMessageChat(msgNbr)
            
        return self.reponse

 
#fin chat
#################################
#fermer serveur

    def shutdown(self):
        leChat.terminer()

#fin fermer serveur
################################


server.register_instance(ControlleurServeur())

# Demarrer la boucle du serveur
try:
    print "serveur demarre"
    print 'Tapez Control-C pour sortir'
    server.serve_forever()
except KeyboardInterrupt:
    #server.shutdown()
    print 'Termine!'



    #IMPORTANT:
    #    * Ne pas accepter deux fois le meme nom dans ConnecterJoueur. OK!!! Teste!
    #    * Effacer messages:
    #            - Quand ils sont lus. pickle le fait de facon automatique!!
    #            - Quand ils sont "repetes". OK!!! Teste!! 
    
            
            
            
            
