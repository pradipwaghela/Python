"""
Kivy :-
Open source patform framework
Allow us to create app for maultiple platform
Support iput filed like keyboard,mouse,muti touch.
Kivy life cycle
run() -> build -> on_start()-> Application Runs -> on_stop() -> Kill app
                                            ^   ->  on_pause() resume? Yes ->   on_resume() -> Application Runs
                                                                ^      no  ->   Kill app
Widgets:-
Key element of  GUI expericence
Event -> Widget -> Response
Event:-
Property event
Widget event
Layout:-
This are container, Which are use to arrange widget as per user need
type:-
Anchor 
Float
Grid
Page 
"""
from kivy.app import App
from kivy.uix.label import Label
from matplotlib.pyplot import cla

class App1(App):
    def build(self):
        return Label(
            text="Hello Wordld"
        )
A1=App1()
A1.run()