from tree.utils.calculs.Variable import Variable

class Variable_time(Variable):
    """
    Store string date variable
    """
    def __init__(self, name, val, action_get = None, action_set = None):
        Variable.__init__(self, name, val, action_get, action_set)

    def get_float(self, inst, variable_name):
        string_time = super().get(inst, variable_name)
        # convert into seconds
        try:
            hours, minutes = string_time.split(":")
        except AttributeError:
            return int(string_time)
        return int(hours)*3600+int(minutes)*60

