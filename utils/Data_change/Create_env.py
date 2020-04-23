from tree.Environnement import Environnement
from tree.Tree import Tree
from utils.Data_change.Create_lumière import get_lumiere
from utils.Data_change.Create_inputs import get_interrupteurs
from utils.Data_change.Create_preset import get_preset
from utils.Data_change.utils.Read import ouvrir, lire, trouver_dossier

def get_env(nom, index):
    """
    retourne un environnement complet
    """
    env = Environnement(nom) 
    print("Environnement : "+ nom)
    
    #on recupére les lumières
    for lumière in lire(ouvrir(nom+"/lumieres.data")):
        env.add_lumiere(get_lumiere(lumière.split("|")))

    # on recupére les presets
    for dossier in trouver_dossier("/"+nom+"/preset"):
        env.add_preset(get_preset(env,index, dossier))

    # on recupére les options
    # on commence par lire tout les informations utiles
    read_preset = False
    for ligne in lire(ouvrir(nom+"/option.data")):
        if ligne.count("Preset") != 0:
            # on lit la table des presets maintenant
            read_preset = True
        else : 
            args = ligne.split("=")
            arg1 = args[0]
            arg2 = args[1]
            if read_preset:
                # on lit des presets
                mode = Tree().get_mode(arg1)
                assert(mode != None)
                preset = env.get_preset(arg2)
                assert(preset != None)
                env.liste_presets_choisis.add(mode, preset)
            else:
                # on lit des paramètres
                # il n'y en a pas encore
                pass
    
    # on met le même mode que le tree
    env.change_mode()
    print("fin env")
    return env 









