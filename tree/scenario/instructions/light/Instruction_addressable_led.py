from tree.scenario.instructions.light.Instruction_light import Instruction_light
from time import sleep, time
import numpy as np
from tree.utils.Logger import Logger

class Instruction_addresable_led(Instruction_light):
    """
    Setup a program for a addressable led
    """
    def __init__(self, calculator, light, dimmer, program, speed, duration, delay, synchro):
        Instruction_light.__init__(self, calculator, light, duration, delay, synchro)
        self.dimmer = dimmer
        self.program = program
        self.speed = speed

    def initialize(self):
        super().initialize()
        self.eval(self.dimmer)
        self.eval(self.speed)
        self.eval(self.program)

    def run(self, barrier=None):
        super().run()
        self.light.connect()
        self.light.set_program(self.eval(self.program))
        sleep(0.2)
        self.light.set_speed_dimmer(self.eval(self.dimmer),self.eval(self.speed))

        self.light.disconnect()
 
    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : Addressable_led\n")
        string += "".join("- Program : {}\n".format(self.program))
        string += "".join("- Speed : {}\n".format(self.speed))
        string += "".join("- Dimmer : {}\n".format(self.dimmer))
        return string   


