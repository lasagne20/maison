from tree.connected_objects.Lamp import Lamp
import time
from In_out.external_boards.relay.Relay import STATE
from tree.utils.Logger import Logger

class Addressable_led(Lamp):
    """
    Addressable led
    """
    def __init__(self, name, relay, controler):
        Lamp.__init__(self, name, relay)
        self.controler = controler
        self.dimmer = 0
        self.speed = 0
        self.program = 1

    def force_relay(self, force):
        if self.relay:
            super().force_relay(force)

    def set_state(self, state):
        if self.relay:
            super().set_state(state)

    def connect(self):
        if not(self.connected):
            if self.program == 1 and not(self.force):
                self.set_state(True)
                time.sleep(3)
            self.connected = self.controler.connect()
            if not(self.connected):
                # the led is out of order
                Logger.error("The led {} is out of order".format(self.name))
                self.set_state(False)
        return self.connected

    def disconnect(self):
        if self.connected:
            if self.program == 1 and not(self.force):
                self.controler.disconnect()
                time.sleep(3)
                self.set_state(False)
                self.connected = False

    def set_speed_dimmer(self, dimmer, speed):
        assert (self.connected), "Need to connect the led before set the speed or dimmer"
        self.speed = speed
        self.dimmer = dimmer
        return self.controler.send_dimmer_speed(self.dimmer, self.speed)

    def set_program(self, program):
        assert (self.connected), "Need to connect the led before set the program"
        self.program = program
        return self.controler.send_prog(self.program)


    def reload(self, other):
        if isinstance(other, Led):
            super().reload(other)
            self.dimmer = other.dimmer
            self.program= other.program
            self.speed= other.speed

    def __eq__(self, other):
        if isinstance(other, Addressable_led):
            return super().__eq__(other)\
                    and self.relay == other.relay\
                    and self.dimmer == other.dimmer\
                    and self.program == other.program\
                    and self.speed == other.speed\
                    and self.controler == other.controler
        return False

    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : Addressable led\n")
        string += "".join("- Status : dimmer={} speed={} prog={}\n".format(self.dimmer, self.speed, self.program))
        string += "".join("- Controler : {}\n".format(self.controler))
        return string


