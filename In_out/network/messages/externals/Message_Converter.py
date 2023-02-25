from tree.utils.Logger import Logger
from In_out.network.messages.interrupt.Press_inter import Press_inter
from In_out.network.messages.interrupt.Change_mode import Change_mode
from enum import Enum

class MacroDroid(Enum):
    press_inter = Press_inter
    change_mode = Change_mode


class App_types(Enum):
    macrodroid = MacroDroid

class Message_Converter:
    """
    Convert string message for external interrupt
    to understanding messages
    """

    @classmethod
    def convert(self, data):
        try:
            type_connection, id_device, message, args = data.decode('utf-8').split("/")
        except:
            Logger.error("Wrong data received")

        return App_types[type_connection].value[message].value(*args.split(","))

