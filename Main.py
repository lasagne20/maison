from web_app.site_maison import Site_maison
from utils.In_out import get_tree
from tree.Tree import Tree

 
"""
Ceci est le code qui sera éxécuter au lancement du site par apache
donc au démarage du rasperry
"""
# on lance tout
# on recupére l'arbre

site = Site_maison()



# on donne à apache la bonne application
app = site.site


if __name__ == "__main__":
     app.run(debug=True)
