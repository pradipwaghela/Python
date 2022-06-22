
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Container(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(self,**kwargs)
        layoutbtn=AnchorLayout(anchor_x='right',
            anchor_y='bottom')
        btn=Button(
            text="Click me",
            size_hint=(.2,.2),
        )
        layoutlbl=AnchorLayout(anchor_x='left',
            anchor_y='bottom')
        lbl1=Label(
            text="Good Mornig",
        )
        layoutbtn.add_widget(btn)
        layoutlbl.add_widget(lbl1)

class App2(App):
    def build(self):
        parent=Container()
        return parent
        
App2().run()

