from In_out.utils.Port_extender import Port_extender
from In_out.cartes.relais.Relais import Relais

class Relais_port_extender(Relais):
    """
    Ceci est un relais
    """
    def __init__(self, extender, port_bus, registre, numero):
        Relais.__init__(self)
        self.port_bus = port_bus
        self.numero = numero
        self.registre = registre
        self.bus = extender

    def reload(self):
        self.bus.write_pin(self.port_bus, self.registre, self.numero, self.etat.value)
