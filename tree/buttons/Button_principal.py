from tree.buttons.Button import Button
from tree.scenario.Scenario import MARKER

class Button_principal(Button):
    """
    Button that use the principal scenario of the environnement
    if there are not a scenar_off, it juste do scenar_on
    """
    def __init__(self, name, manager, scenar_on, scenar_off = None):
        Button.__init__(self, name, manager)
        self.scenar_on = scenar_on
        self.scenar_off = scenar_off

    def state(self):
        return self.scenar_on.state()

    def press(self, state = None):
        if self.scenar_off:
            # if there are 2 scenarios
            if not(state):
                state = (self.manager.get_marker() == MARKER.ON)

            if state:
                self.manager.do_scenar_principal(self.scenar_off)
            else:
                self.manager.do_scenar_principal(self.scenar_on)
        else:
            # simple button, juste do the scenar_on
            self.manager.do_scenar_principal(self.scenar_on)


