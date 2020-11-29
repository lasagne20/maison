from tree.connected_objects.Connected_object import Connected_object
from time import sleep
from threading import Lock
from In_out.cartes.relais.Relais import Etat
from utils.Logger import Logger

class Lamp(Connected_object):
    """
    A simple ON/OFF lamp 
    """
    def __init__(self, name, relay, invert = False):
        Connected_object.__init__(self, name)
        self.relay =  relay
        self.invert = invert
        self.force = False
        self.connected = False

    def set(self, on_off):
        self.set_relay(on_off)

    def connect(self):
        if not(self.connected):
            if not(self.force):
                self.set_relay(True)
            self.connected = True

    def disconnect(self):
        if self.connected:
            if not(self.force):
                self.set_relay(False)
            self.connected = False

    def force_relay(self, force):
        # force the relay always to ON
        self.force = force
        if force:
            self.set_relay(Etat.ON)
        elif not(self.connected):
            self.set_relay(Etat.OFF)

    def set_relay(self, on_off):
        if self.invert:
            on_off = not(on_off)

        if on_off:
            etat = Etat.ON
        else:
            etat = Etat.OFF
        if self.relay.etat != etat:
            self.relay.set(etat)

    def etat(self):
        return self.relay.etat
