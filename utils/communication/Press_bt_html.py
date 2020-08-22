from tree.Tree import Tree
from utils.communication.Message import Message

class Press_bt_html(Message):

    def __init__(self, nom_env, numero):
        self.nom_env = nom_env
        self.numero = numero

    def do(self):
        Tree().press_bouton_html(self.nom_env, self.numero)