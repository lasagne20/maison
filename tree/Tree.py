from tree.Environnement import Environnement
from threading import Thread
from utils.Logger import Logger
from tree.utils.List_radio import List_radio

class Tree:
    """
    This static class allow to access all the environnements at any time
    It also manage modes
    """

    global_environnement = Environnement("GENERAL")
    list_modes = Liste_radio()

    @classmethod
    def get_mode(self, name_mode):
        return self.list_modes.get(name_mode)

    @classmethod
    def change_mode(self, name_mode):
        mode_select = self.list_modes.get(name_mode)
        self.list_modes.change_select(mode_select)
        self.global_environnement.change_mode(mode_select)

    @classmethod
    def add_mode(self, mode):
        self.list_modes.add(mode)

    @classmethod
    def get_current_mode(self):
        return self.list_modes.selected()

    @classmethod
    def get_env(self, path):
        path = path.split(".")
        return self.global_environnement.get_env(path)

    @classmethod
    def get_names_envi(self):
        return self.global_environnement.get_names_envi()

    @classmethod
    def press_inter(self, name_env, name):
        Logger.info("press inter {}, env = {}".format(name_env, name))
        self.get_env(name_env).press_inter(name)

    @classmethod
    def get_scenar(self, name_env, name_scenar, preset=None):
        return self.get_env(name_env).get_scenar(name_scenar, preset)
