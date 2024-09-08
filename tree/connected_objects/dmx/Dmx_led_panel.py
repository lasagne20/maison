from tree.connected_objects.dmx.Dmx_strip_led import Dmx_strip_led
from tree.connected_objects.dmx.Dmx_device import Dmx_device
from enum import Enum

class Dmx_led_panel(Dmx_strip_led):
    """
    Led panel connected by dmx
    """
    def __init__(self, name, relay, addr, dmx, color = "0x000000"):
        Dmx_strip_led.__init__(self, name, relay, addr, dmx, color)
        self.white = 0

    def connect(self):
        if self.color.is_black() and not(self.force) and self.white == 0:
            self.set_state(True)
        Dmx_device.connect(self)
        return True

    def disconnect(self):
        if self.color.is_black() and not(self.force) and self.white == 0:
            self.set_state(False)
        Dmx_device.disconnect(self)



    def set_white(self,dimmer, white):
        self.white = white
        dimmed_white = int(white * dimmer/100)
        super().set(CHANNEL.white, dimmed_white)

class CHANNEL(Enum):
    red = 1
    green = 2
    blue = 3
    white = 4

