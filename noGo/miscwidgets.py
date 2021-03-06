from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty, AliasProperty, StringProperty, DictProperty, BooleanProperty, StringProperty, OptionProperty

class AndroidTextInput(TextInput):
    def on_focus(self,*args):
        print 'focus changed for',self
        super(AndroidTextInput, self).on_focus(*args)
        

class CarouselRightArrow(Button):
    pass
class CarouselLeftArrow(Button):
    pass

class VDividerLine(Widget):
    vgap = NumericProperty(0.2)
    linewidth = NumericProperty(1)
    colour = ListProperty([0.195,0.641,0.805])

class HDividerLine(Widget):
    hgap = NumericProperty(0.1) 
    linewidth = NumericProperty(2)
    colour = ListProperty([0.195,0.641,0.805])

class DividerLine(Widget):
    hgap = NumericProperty(0.1) 
    linewidth = NumericProperty(2)
    colour = ListProperty([0.195,0.641,0.805])

class WhiteStoneImage(Widget):
    pass
class BlackStoneImage(Widget):
    pass

class NumberChooser(BoxLayout):
    number = NumericProperty(0)
    number_max = NumericProperty(9)
    number_min = NumericProperty(0)
    def increment(self):
        if self.number < self.number_max:
            self.number += 1
    def decrement(self):
        if self.number > self.number_min:
            self.number -= 1

