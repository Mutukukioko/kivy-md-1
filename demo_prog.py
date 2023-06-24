from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class DemoApp(App):

    def build(self):
        layout = AnchorLayout(
            anchor_x = 'left', anchor_y = 'top'
        )
        bttn1 = Button(
            text = "Anchor layout",
            size_hint = (.15, .15),
            background_color = (22, 25.86, 1.0),
            color = (0,0,0,1)
        )
        layout.add_widget(bttn1)
        return layout
    
demo = DemoApp()
demo.run()