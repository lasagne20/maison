import socket
from In_out.wifi_devices.Wifi_device import Wifi_device
from time import sleep
import binascii

class H806SB(Wifi_device):
    """
    Addressable led controller
    """
    def __init__(self, ip):
        Wifi_device.__init__(self, ip)
        self.server_address = ('1.1.1.1', 4626)

    def connect(self, attempts = 20):
        # For now it is automaticaly connected when the device
        # turn on, need to add a modif in dhcp file if alredy connected
        # to a wifi network
        self.controler = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for i in range(0, attempts):
            try:
                self.controler.bind((self.ip, 0))
                return True
            except Exception as e:
                sleep(1+i*0.5)
        return False

    def send_prog(self, number):
        print(f"send, program:{number}")
        prgm = str(format(3+number, "02X")+format(number-1,"02x")).lower()
        hex_message_prog = f'fbc5{str(prgm)}b23a0c00'
        message= binascii.unhexlify(hex_message_prog)
        self.controler.sendto(message, self.server_address)

    def send_dimmer_speed(self, dimmer, speed):
        print(f"send, dimmer:{dimmer}, speed:{speed}")
        format_dim = str(format(int(dimmer * 0x1F / 100), "02X")).lower()
        format_speed = str(format(int((speed) * 0x1F / 100 + 1), "02X")).lower()
        hex_message= f'fbc1ff{format_speed}{format_dim}0100a8003a0c00b23a0c00'
        message = binascii.unhexlify(hex_message)
        self.controler.sendto(message, self.server_address)


    def disconnect(self, is_black=True):
        self.controler.close()
        self.controler = None

