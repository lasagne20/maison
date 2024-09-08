#!/usr/bin/env python3
import sys
from In_out.network.Client import Client
from In_out.network.messages.interrupt.Press_inter import Press_inter

def main():
    if len(sys.argv) < 2:
        raise(Exception("Usage : env_name inter_name"))
    else:
        message = Press_inter(sys.argv[1], sys.argv[2], None)
    client = Client()
    client.start()
    print(client.send(message))
    client.disconnect()

if __name__ == "__main__":
    main()

