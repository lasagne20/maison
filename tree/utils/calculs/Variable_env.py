from tree.utils.calculs.Variable import Variable
from tree.Tree import Tree

class Variables_env(Variable):
    """
    Allow to find a variable in another env
    """
    def __init__(self):
        Variable.__init__(self, "general", 0)

    def get(self, path_env, variable_name):
        env = Tree().get_env(path_env)
        var = env.get_variable(variable_name)
        if var:
            return var.get()
        # it can be a state variable
        if variable_name.count("state"):
            return env.is_on()
        raise(Exception("The variable {} in the environnement {} doesn't existe".format(variable_name, path_env)))

    def set(self, val):
        raise(Exception("Cannot set an this variable"))
        

