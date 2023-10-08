from tree.scenario.instructions.Instruction import Instruction
from enum import Enum
from time import time, sleep

class Instruction_store(Instruction):
    """
    Up or down the store
    """
    def __init__(self,calculator, store, percent, duration, delay, synchro):
        Instruction.__init__(self, calculator, duration, delay, synchro)
        self.store = store
        self.percent = percent

    def run(self, barrier = None):
        """
        Setup a try/finally to allow kill from another instruction
        """
        try:
            self.store.lock()
            current_state = self.store.get_percent_closed()
            print(current_state, self.percent)
            if self.percent == -1:
                self.store.stop()
                return

            waiting_time = abs(current_state-self.percent)/100*self.store.time_off_closing
            if current_state > self.percent:
                # go up
                self.store.up()
            elif current_state < self.percent:
                # go down
                self.store.down()

            if self.percent == 100 or self.percent == 0:
                # To be sure we are at the end
                waiting_time += 10

            for i in range(0, int(waiting_time)):
                assert not self.store.test()
                sleep(1)
                self.store.increment(1)

            if self.percent != 100 and self.percent != 0:
                self.store.stop()

        except AssertionError:
            #The inst what killed
            pass
        finally:
            if not self.store.test() and self.percent != -1:
                self.store.set_percent_closed(self.percent)
            self.store.unlock()

    def finish(self):
        super().finish()
        self.store.kill()

    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : store\n")
        return string
