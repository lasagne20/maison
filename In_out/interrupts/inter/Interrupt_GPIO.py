from time import time
from tree.Tree import Tree
from In_out.interrupts.inter.Interrupt import Interrupt
from time import sleep
try:
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()

class Interrupt_GPIO(Interrupt):
    """
    It is a GPIO interrupt
    """
    def __init__(self, name, name_env, pin, client):
        Interrupt.__init__(self, name, name_env, client)
        self.pin = pin
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(pin, GPIO.RISING, callback=self.press)
        self.value = GPIO.input(pin)

    def press(self, event):
        if (self.value != GPIO.input(event) and GPIO.input(event) == 1):
            super().press()
        self.value = GPIO.input(event)

    def __str__(self):
        return "type : gpio | pin : {}".format(self.pin)
