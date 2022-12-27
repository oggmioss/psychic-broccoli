import kivy
from kivy.app import App
import BoxLayout

kivy.require('2.0.0')

class GameView(BoxLayout):
    def __init__self():
        super(GameView, self).__init__()

class AnthoApp(App):
    def build(self):
        return GameView()

anthoApp = AnthoApp()
anthoApp.run()