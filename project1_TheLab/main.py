from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from numpy import angle

class ImagesExample(GridLayout):
    speed = 0
    def on_slider_value(self, widget):
        self.speed = widget.value

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    #slider_value_txt = StringProperty("value")

    def on_button_click(self):
        print("Button clicked")
        self.count += 1
        self.my_text = str(self.count)
        
    def on_toggle_button_state(self, widget):
        print("Toggle state: "+ widget.state)
        if widget.state == "normal":
            #OFF
            widget.text = "OFF"
            self.count_enabled = False
        else:
            #ON
            widget.text = "ON"
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print("Switch active: "+ str(widget.active))
        
    def on_slider_value(self, widget):
        print("Slider value: "+ str(int(widget.value)))
        #self.slider_value_txt = str(int(widget.value))
    
    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'lr-tb'
        for i in range(0, 100):
            #size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint= (None, None), size = (size, size))
            self.add_widget(b)

#class GridLayoutExample(GridLayout):
#    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
'''    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        b1 = Button(text = "A")
        b2 = Button(text = "B")
        b3 = Button(text = "C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    pass
'''

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()