from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        title: "NETFLIX"
        md_bg_color: (200, 0, 0, 255)
        elevation: 4
        right_action_items:  
            [
            ["home", "", "Home"],
            ["message-star", "", "starred Messages"],
            ["message-question", "" , "Message question"],
            ["message-reply", "", "Message reply"],
            ]
            
    MDNavigationRail:
        MDNavigationRailItem:
            text: "Python"
            icon: "language-python"
        MDNavigationRailItem:
            text: "JavaScript"
            icon: "language-javascript"
        MDNavigationRailItem:
            text: "CPP"
            icon: "language-cpp"
        MDNavigationRailItem:
            text: "Git"
            icon: "git"
    MDScreen:
'''
class Example(MDApp):
    def build(self):
        return Builder.load_string(KV)
Example().run()