from tree.utils.List import List
from random import randint
from tree.scenario.Scenario import MARKER
from tree.utils.Logger import Logger
import re
from datetime import datetime

def time():
    # return the time of the day in second
    t = datetime.now().time()
    return (t.hour * 60 + t.minute) * 60 + t.second

class Calculator:
    """
    Calculate the expressions
    """
    def __init__(self):
        self.variables = List()

    def add(self, var):
        try:
            self.variables.get(var.name)
            Logger.warn("The variable {} is already present".format(var.name))
        except (KeyError, ValueError):
            self.variables.add(var)

    def eval(self, expression, inst=None):
        string = str(expression)
        if string:
            # search for variables names
            for var in re.split("[\\*,\\-,\\+,\\/,\\(,\\),<,>,&,|,==,\\],\\[,!= ]", string):
                if not(var):
                    continue
                try:
                    int(var)
                except ValueError:
                    try:
                        int(var, 16)
                    except ValueError:
                        if var not in ("False", "True", "not", "randint", "time", "in"):
                            # replace the var_name by it's value
                            string = string.replace(var,"self.get_value(\"{}\",expression, inst)".format(var))
            try:
                return eval(string)
            except (SyntaxError, TypeError) as e:
                expression.raise_error(f"{e} in {string}")

    def get_value(self, var_name, expression, inst):
        try:
            return float(var_name)
        except ValueError:
            cutted_name = var_name.split(".")[0]
            try:
                return self.variables.get(cutted_name).get_float(inst, var_name)
            except KeyError:
                expression.raise_error("Could not find the variable {}".format(var_name))

    def reset(self):
        # reset the inst list of all variables
        for var in self.variables:
            var.reset()


    def get(self, name):
        cutted_name = name.split(".")
        return self.variables.get(cutted_name[0])

    def get_list_variables(self):
        return self.variables

    def __str__(self):
        return str(self.variables)

