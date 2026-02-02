from kivy.app import App
from kivy.uix.button import Button
class Main(App):
 def build(self): return Button(text='РАБОТАЕТ!')
Main().run()