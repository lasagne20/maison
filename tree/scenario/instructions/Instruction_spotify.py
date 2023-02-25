from tree.scenario.instructions.Instruction import Instruction
from tree.utils.Logger import Logger
from enum import Enum
import time

class TYPE_INST_SPOTIFY(Enum):
    start = 0
    stop = 1
    volume = 2
    next_track = 3
    start_playlist = 4


RESOLUTION = 1
class Instruction_spotify(Instruction):
    """
    Modifie spotify values like volumes, play/pause..
    """
    def __init__(self,calculator, spotify, type_inst, val, delay, duration, synchro):
        Instruction.__init__(self,calculator, duration, delay, synchro)
        self.type_inst = type_inst
        self.spotify = spotify
        self.val = val

    def run(self, barrier=None):
        Logger.info(f"{self.type_inst} spotify")
        if self.type_inst == TYPE_INST_SPOTIFY.start:
            self.spotify.start()
        elif self.type_inst == TYPE_INST_SPOTIFY.stop:
            self.spotify.stop()
        elif self.type_inst == TYPE_INST_SPOTIFY.volume:
            self._set_volume()
        elif self.type_inst == TYPE_INST_SPOTIFY.start_playlist:
            self.spotify.start(context_uri=str(self.val))
        elif self.type_inst == TYPE_INST_SPOTIFY.next_track:
            self.spotify.next_track()

    def _set_volume(self):
        try:
            self.spotify.lock()
            super().run()
            final = self.eval(self.val)
            val = self.spotify.get_volume()
            gap = final - val
            if gap == 0:
                return
            nb_dots = self.duration*RESOLUTION
            if val == 0 and not self.spotify.is_started():
                self.spotify.start()
            for _ in range(0,nb_dots):
                assert not self.spotify.test()
                temps = time.time()
                self.spotify.set_volume(int(val))
                val += gap/nb_dots
                dodo = 1/RESOLUTION-(time.time()-temps)
                if dodo > 0:
                    time.sleep(dodo)
            self.spotify.set_volume(int(final))
            if int(final) == 0 and self.spotify.is_started():
                self.spotify.stop()
            Logger.info(f"Set spotify volume to {final}")
        except AssertionError:
            # the inst was killed
            pass
        finally:
            self.spotify.unlock()


    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : spotify\n")
        string += "".join("- Action : {}\n".format(self.type_inst))
        string += "".join("- Args : {}\n".format(self.val))
        return string
