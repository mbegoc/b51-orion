#!/usr/bin/env python


#ce fichier teste le threading pour gerer les evenements simultanes.


import threading
import time


import modele.Vaisseau as Vaisseau


class TestThreads(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        global ship
        ship = Vaisseau.Vaisseau(0,0)
        ship.moveVaisseau(100,400)

        print 'vitesse',
        print ship.vitesseX,
        print ship.vitesseY

    def run(self):
        while ship.deplacement():
            time.sleep(0.2)
            print ship.x,
            print ship.y



test = TestThreads()
test.start()
print "allo"
print "allo"
print "allo"
