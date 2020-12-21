from enum import Enum
from time import sleep
from threading import Thread, Barrier
import uuid

class STATE(Enum):
    CONTINUE = 0
    WAIT = 1

class Instruction():
    """
    This class is the parent class of all instructions
    """
    def __init__(self, calculator, duration, delay, synchro):
        self.delay = delay
        self.duration = duration
        self.synchro = synchro
        self.calculator = calculator

    def run(self, time_spent = 0):
        self.duration=self.eval(self.duration)
        self.delay.wait(time_spent)
        # next in sub-classes

    def finish(self):
        pass

    def eval(self, string):
        return self.calculator.eval(string)

    def initialize(self):
        # verify if the expressions given can be resolved
        self.delay.initialize()
        self.eval(self.duration)

    def __eq__(self, other):
        return True

    def __str__(self):
        string = "- Duration : {}\n".format(self.duration)
        string += "".join("- Delay : {}\n".format(self.delay))
        return string