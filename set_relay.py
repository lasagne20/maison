#!/usr/bin/env python3
from In_out.network.Client import Client
from In_out.network.messages.set.Set_relay import Set_relay
import sys

if len(sys.argv) > 2:
    client = Client()
    client.start()
    port, board = sys.argv[1].split(":")
    client.send(Set_relay([int(port), board], int(sys.argv[2])))
    client.disconnect()
else:
    print("Usage: set_relay.py {addr}:{board} {value}")
