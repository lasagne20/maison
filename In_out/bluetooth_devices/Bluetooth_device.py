from enum import Enum
from In_out.utils.Bluetooth import Bluetooth
from time import sleep


def hex_to_byte(valeur):
        # converti un string hex en byte
        valeur = int(valeur,16)
        return valeur.to_bytes((valeur.bit_length()+7)//8,'big')

class Bluetooth_device:
    """
    Petit boitier bluetooth pour les leds connectées
    """
    def __init__(self, addr, uuid, char_id):
        self.addr = addr
        self.periph = None
        self.char = None
        self.uuid = uuid
        self.char_id = char_id

    def connect(self):
        compt = 0
        while self.periph == None:
            self.periph = Bluetooth().connect(self.addr)
            if self.periph: #!=None
                break
            else:
                compt += 1
                print("La led n'arrive pas à ce connecter")
                sleep(1)
            if compt > 10:
                self.periph = Bluetooth().connect_by_scan(self.addr)
            if compt > 12:
                return 1
        self.char = Bluetooth().get_char(self.periph, self.uuid, self.char_id)
        return 0

    def send(self, valeur):
        Bluetooth().send(self.char, hex_to_byte(valeur))

    def deconnect(self):
        Bluetooth().deconnect(self.periph)
        self.periph = None
        self.char = None





