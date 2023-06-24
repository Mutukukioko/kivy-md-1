from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button


class Float_Layout_Demo(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bttn1 = Button(
            text = "Button 1",
            size_hint =(0.4, 0.4),
            pos_hint = {
            "x":0.3,
            "y":0.3
            }
        )
        self.add_widget(self.bttn1)
        self.bttn2 = Button(
            text = "Button 2",
            size_hint =(0.1, 0.2),
            pos_hint = {
            "x":0.8,
            "y":0.7
            }
        )
        self.add_widget(self.bttn2)



class DemoApp(App):
    def build(self):
        return Float_Layout_Demo()
    
DemoApp().run()