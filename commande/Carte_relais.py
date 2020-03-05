from commande.Bus import Bus
from commande.Carte import Carte
from commande.Relais import Relais

class Carte_relais(Carte):
    """
    Une carte de relais
    """
    def __init__(self, numero, port_bus, registre = 0x12, nb_ports = 8):
        Carte.__init__(self, numero, port_bus, registre, nb_ports)
        self.liste_relais = [ Relais(port_bus, registre, i) for i in range(1,nb_ports+1)]
        for i,pin in enumerate(Bus().read(port_bus, registre)):
            self.liste_relais[i].etat = pin

    def get_relais(self, indice_relais):
        return self.liste_relais[indice_relais-1]
        


