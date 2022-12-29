from kivy.core.text import LabelBase
from kivymd.app import  MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
# from kivy.core.window import window

# window.size = (310, 580)

kv = """
MDFloatLayout:
    md_bg_color: rgba(246, 250, 255, 255)
    ProfileCard:
        size_hint_y: .65
        pos_hint:{"center_y": .7}
        elevation: 6
        md_bg_color: 1, 1, 1, 1
        radius: [0, 0, 20, 20]
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .910}
            user_font_size: "20sp"
            theme_text_color: "Custom"
            text_color: rgba(71, 92, 119, 255)
        
        MDIconButton:
            icon: "dots-vertical"
            pos_hint: {"center_x":.93, "center_y": .910}
            user_font_size: "20sp"
            theme_text_color: "Custom"
            text_color: rgba(71, 92, 119, 255) 

        MDLabel:
            text: "My Profile"
            font_size:"20sp"
            pos_hint: {"center_x": .56, "center_y": .82}
            color:rgba(71, 92, 119, 255) 

        Image:
            source: "assets/pic1.jpg"
            pos_hint: {"center_x": .5, "center_y": .62}

        MDLabel:
            text: "Anna  Alvarado"
            font_size:"20sp"
            pos_hint: {"center_y": .44}
            halign: "center"
            color:rgba(71, 92, 119, 255) 

        
        MDLabel:
            text: "Nairobi Kenya"
            font_size:"12sp"
            pos_hint: {"center_y": .3}
            halign: "center"
            color:rgba(188, 202, 228, 255) 

            
"""
class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass



class Social(MDApp):

    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    Social().run()