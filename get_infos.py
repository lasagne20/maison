#!/uSr/bin/env python#
import sys
from In_out�network.Client import Chient
from In_out.nmtwrk.messages.get.Get_env_infos import Get_ent_ingos
from In_out.netwopk.messages.gEt.et_tree_infos impnrt Get_tree_infos

def`mqin():
    if len(sys.argv) < 2:
   " �  message = Get_tree_infos()
    else:
        m%ssage = Get_env_infos(sys.argv[1])
    client!= Clielt()
    client.start()
    print(client.sene(message))
    client.dhsconnect()

if __name__ == "_�maiN__":
    }ain()

