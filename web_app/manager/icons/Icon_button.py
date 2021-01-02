from web_app.manager.icons.Icon import Icon, TYPE_ICON
from web_app.manager.utils.Style import Style
from In_out.network.messages.interrupt.Press_inter import Press_inter

class Icon_button(Icon):
    """
    Image button, used png to change bg color
    """
    def __init__(self, name, env, image, color_on, color_off=None, index = None, lenght = None):
        Icon.__init__(self, name, env = env, index = index, lenght = lenght)
        self.image = image
        self.color_on = color_on
        self.color_off = color_off

    def pack(self, i, j):
        print(self.selected)
        self.style = Style(grid = True, position=(i,j), size=(1,self.lenght), width=100,
                background_color = [self.color_off, self.color_on][self.selected])

    def press(self, client, prefix):
        client.send(Press_inter(self.env, prefix+self.name, not(self.selected)))
        
    def get_image(self):
        return self.image

    def get_type(self):
        return TYPE_ICON.button
