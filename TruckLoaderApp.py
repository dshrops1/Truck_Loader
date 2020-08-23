#main app
import kivy
kivy.require("1.11.1")

from kivy.app import App
from kivy.uix.widget import Widget
from components import onStart

class MainWidget(App):

    def build(self):
        return Widget()


if __name__ == '__main__':
    onStart.onOpeningSequence()
    MainWidget().run()
