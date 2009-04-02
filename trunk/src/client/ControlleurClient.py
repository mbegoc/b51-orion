import xmlrpclib
import affichage


class Controlleur(object):
    def __init__(self):
        self.vue=affichage
        self.serveur=xmlrpclib.ServerProxy('http://localhost:8000')
        self.vue.root.mainloop()
        