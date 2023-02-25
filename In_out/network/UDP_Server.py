import socket
from tree.utils.Logger import Logger
from In_out.network.Client import Client
from In_out.network.messages.externals.Message_Converter import Message_Converter
import netifaces

class UDP_Server:
    """
    Allow to communicate udp to the tcp server (tree)
    """
    def __init__(self, client, port=1234):
        self.ip = netifaces.ifaddresses('eth0')[netifaces.AF_INET][0]['addr']
        self.port = port
        self.client = client
        self.converter = Message_Converter()

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))

    def start(self):
        Logger.info("Starting UPD Server")
        while True:
            data, address = self.socket.recvfrom(4096)
            self.client.send(self.converter.convert(data))


