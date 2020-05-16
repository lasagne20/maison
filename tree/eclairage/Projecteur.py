from tree.eclairage.Lumiere import Lumiere
from In_out.cartes.Relais import Etat
from In_out.utils.ST_nucleo import ETAT_TRIAC
from enum import Enum
from threading import Lock
from time import sleep

class LAMPE(Enum):
    # type  = (maxi,mini)
    type_plafond = (400,130)
    type_poutre = (400,130)
    type_63 = (430,80)
    type_91 = (430,50)
    type_64 = (430,180)
    type_73 = (400,130)
    type_61 = (430,250)


class Projecteur(Lumiere):
    """
    Un projecteur simple sur un dyrak
    """
    def __init__(self, nom, triak, type_lampe, relais = None):
        Lumiere.__init__(self, nom)
        self.triak = triak
        self.relais = relais
        self.type_lampe = type_lampe
        self.dimmeur = 0
        self.mutex = Lock()
        # on eteint la lampe sur la carte
        self.triak.set(10**9,ETAT_TRIAC.off)

    def connect(self):
        self.mutex.acquire()
        #on connect s'il faut
        if self.dimmeur == 0:
            # on met le triac en place
            self.triak.set(self.convert(0))
        elif self.dimmeur == 100:
            # on met le projo en dimmage
            self.triak.set(self.convert(100))

    def deconnect(self):
        #on deconnect s'il faut
        if self.dimmeur == 0:
            # on met la valeur max pour éteindre la lampe
            self.triak.set(10**9, ETAT_TRIAC.off)
        elif self.dimmeur == 100:
            # on met le projo à on
            self.triak.set(10**9, ETAT_TRIAC.on)
        self.mutex.release()

    def set(self, dimmeur):
        valeur = self.convert(dimmeur)
        self.triak.set(valeur)
        self.dimmeur = int(dimmeur)

    def convert(self, dimmeur):
        # conversion du dimmeur en valeur triac
        maxi, mini = self.type_lampe.value
        valeur = int(mini + (maxi-mini)*(1-dimmeur/100))
        print(valeur)
        return valeur



    def show(self):
        print("nom = " + self.nom)

        
