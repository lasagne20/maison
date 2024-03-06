import numpy as np
from tree.scenario.instructions.light.Instruction_light import Instruction_light, RESOLUTION
from tree.utils.Color import Color
import time
from tree.utils.Logger import Logger

class Instruction_rgbw(Instruction_light):
    """
    Instruction for a RBG colors light
    """
    def __init__(self, calculator, light, dimmer, duration, delay, synchro, color, white):
        Instruction_light.__init__(self, calculator, light, duration, delay, synchro)
        self.color = color
        self.dimmer = dimmer
        self.white = white

    def initialize(self):
        super().initialize()
        self.eval(self.white)
        self.eval(self.dimmer)
        self.eval(self.color)

    def run(self, barrier=None):
        delay = time.time()
        
        try:
            self.light.lock()
            dimmer_final = self.eval(self.dimmer)
            dimmer_initial = self.light.dimmer
            color = Color(self.eval(self.color))
            white_final = self.eval(self.white)
            white_initial = self.light.white
            Logger.debug("Set led {} to {}, white:".format(self.light.name, color, white_final))
            if self.eval(self.duration) == 0:
                if dimmer_final != dimmer_initial or color != self.light.color or white_final != white_initial:
                    if self.light.connect():
                        super().run(time_spent=(time.time()-delay))
                        self.light.set_color(dimmer_final, color.value)
                        self.light.set_white(dimmer_final, white_final)
                        self.light.disconnect()
                return

            if (dimmer_final == dimmer_initial and color == self.light.color and white_final == white_initial):
                if barrier is not None:
                    barrier.wait()
                return
            nb_dots = RESOLUTION*self.eval(self.duration)
            if dimmer_initial != dimmer_final:
                liste_dimmer = np.arange(dimmer_initial, dimmer_final, (dimmer_final-dimmer_initial)/nb_dots)
            else:
                liste_dimmer = [dimmer_initial]*nb_dots

            if white_initial != white_final:
                liste_white = np.arange(white_initial, white_final, (white_final-white_initial)/nb_dots)
            else:
                liste_white = [white_initial]*nb_dots
            liste_color = color.generate_array(self.light.color, nb_dots)


            connected = self.light.connect()
            if not(connected):
                if barrier is not None:
                    barrier.wait()
                return
            super().run(time_spent=(time.time()-delay))
            assert not self.light.test()

            if barrier is not None:
                barrier.wait()
            for dim, value_color, white in zip(liste_dimmer, liste_color, liste_white):
                assert not self.light.test()
                self.light.set_color(dim, value_color)
                self.light.set_white(dim, white)
                time.sleep(1/RESOLUTION)
                if barrier is not None:
                    barrier.wait()
            self.light.set_color(dimmer_final, color.value)
            self.light.set_white(dimmer_final, white_final)
            self.light.disconnect()
        except AssertionError:
            # The inst is killed
            pass

        finally:
            self.light.unlock()

    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : color\n")
        string += "".join("- Color : {}\n".format(self.color))
        string += "".join("- White : {}\n".format(self.white))
        string += "".join("- Dimmer : {}\n".format(self.dimmer))
        return string   


