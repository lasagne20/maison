from tree.connected_objects.Connected_object import Connected_object
from enum import Enum
from time import sleep
from threading import Lock
from In_out.external_boards.relay.Relay import STATE as STATE_RELAY

class STATES(Enum):
    CLOSING = 1
    OPENNING = 2
    STOP = 3

class Store(Connected_object):
    """
    Up / Down store
    """
    def __init__(self,name, relay_up_down, relay_on_off, time_off_closing):
        Connected_object.__init__(self, name)
        self.relay_on_off = relay_on_off # this relay is inverted
        self.relay_up_down = relay_up_down
        self.time_off_closing = time_off_closing
        self.percent_closed = 0 # by default all relay are open, and store are up
        self.state = STATES.STOP

    def get_percent_closed(self):
        return self.percent_closed

    def set_percent_closed(self, percent_closed):
        self.percent_closed = percent_closed

    def increment(self, second):
        """Increment the percent_closed to the number of specified seconds"""
        new_val = max([min([second/self.time_off_closing*100,100]), 0])
        if self.state == STATES.OPENNING:
            new_val = -new_val
        self.set_percent_closed(self.percent_closed+new_val)

    def up(self):
        print("up")
        self.relay_on_off.set(STATE_RELAY.OFF, force=True)
        self.relay_up_down.set(STATE_RELAY.OFF, force=True)
        self.state = STATES.OPENNING

    def down(self):
        print("down")
        self.relay_on_off.set(STATE_RELAY.OFF, force=True)
        self.relay_up_down.set(STATE_RELAY.ON, force=True)
        self.state = STATES.CLOSING

    def stop(self):
        print("stop")
        self.relay_on_off.set(STATE_RELAY.ON, force=True)
        self.relay_up_down.set(STATE_RELAY.OFF, force=True)
        self.state = STATES.STOP

    def reload(self, other):
        if isinstance(other, Store):
            super().reload(other)
            self.percent_closed == other.percent_closed
            self.time_off_closing == other.time_off_closing

    def __eq__(self, other):
        if isinstance(other, Store):
            return super().__eq__(other)\
                    and self.relay_up_down == other.relay_up_down\
                    and self.relay_on_off == other.relay_on_off\
                    and self.percent_closed == other.percent_closed
        return False

    def __str__(self):
        string = super().__str__()
        string += "".join("- Type : Stores\n")
        return string




