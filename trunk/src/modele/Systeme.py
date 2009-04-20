# un systeme stellaire
# un systeme stellaire a une position fixe 
# dans l'espace est ne fait pas grand chose a part ca
import random

class Systeme(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.id = random.randint(0,100)
        self.conquerant = "null"
        
