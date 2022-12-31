from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivymd.effects.fadingedge.fadingedge import FadingEdgeEffect
from kivymd.uix.list import OneLineListItem


KV = '''
MDScreen:
    FadeScrollView:
        fade_height: self.height / 2
        fade_color: root.md_bg_color
    MDList:
        id: container
'''


class FadeScrollView(FadingEdgeEffect, ScrollView):
    pass
class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
    def on_start(self):
        for i in range(20):
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Single-line item {i}")
    )
Test().run()
