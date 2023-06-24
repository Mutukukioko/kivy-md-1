from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.button import Button


class Page_Layout_Demo(PageLayout):
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
        


class DemoApp(App):
    def build(self):
        return Page_Layout_Demo()
    

DemoApp().run()