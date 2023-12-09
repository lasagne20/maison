from tree.utils.List import List
from random import randint
from tree.scenario.Scenario import MARKER
from tree.utils.Logger import Logger
from datetime import datetime
import re

MORNING = (4, 9) # hours

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
            for var in re.split("[\\*,\\-,\\+,\\/,\\(,\\),<,>,|,==,!=, &]", string):
                if not(var):
                    continue
                try:
                    int(var)
                except ValueError:
                    try:
                        int(var, 16)
                    except ValueError:
                        if var not in ("False", "True", "not", "randint", "morning"):
                            # replace the var_name by it's value
                            var = var.split("[")[0]
                            string = string.replace(var,"self.get_value(\"{}\",expression, inst)".format(var))
                        elif var == "morning":
                            # check if it is the morning
                            now = datetime.now()
                            before = now.replace(hour=MORNING[0], minute=0, second=0, microsecond=0)
                            after = now.replace(hour=MORNING[1], minute=0, second=0, microsecond=0)
                            string = str((before<now) and (now<after))

            try:
                return eval(string)
            except SyntaxError as e:
                expression.raise_error(str(e))
            except ValueError as e:
                Logger.error(e)
        return 0

    def get_value(self, var_name, expression, inst):
        try:
            value = float(var_name)
        except ValueError:
            cutted_name = var_name.split(".")[0]
            try:
                value = self.variables.get(cutted_name).get(inst, var_name)
            except KeyError:
                expression.raise_error("Could not find the variable {}".format(var_name))
        if value is None:
            raise ValueError(f"The variable {var_name} is None")
        return value

    def reset(self):
        # reset the inst list of all variables
        for var in self.variables:
            var.reset()

    def change_variable(self, name, value):
        self.variables.get(name).set(value)

    def get(self, name):
        cutted_name = name.split(".")
        return self.variables.get(cutted_name[0])

    def get_list_variables(self):
        return self.variables

    def __str__(self):
        return str(self.variables)

