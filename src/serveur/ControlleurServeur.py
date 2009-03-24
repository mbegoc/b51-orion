from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import datetime


# Creer un serveur
server = SimpleXMLRPCServer(("localhost", 8000),
                            requestHandler=SimpleXMLRPCRequestHandler)
server.register_introspection_functions()

# Enregistrer l'instance d'une classe
#Toutes ses fonctions vont etre publiees
class Serveur:
    def __init__(self):
        pass
        
    def uneFonction(self):
        pass
    
server.register_instance(Serveur())

# Demarrer la boucle du serveur
print "OK, serveur demarrer"
server.serve_forever()
print "OK, serveur arreter"
