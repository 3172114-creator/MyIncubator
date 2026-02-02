


































from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class CalcApp(App):
    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=10)
        self.lbl = Label(text="0", font_size=40, size_hint=(1, .4), halign="right")
        bl.add_widget(self.lbl)

        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .6))
        btns = ["7","8","9","/", "4","5","6","*", "1","2","3","-", "C","0","=","+"]
        
        for b in btns:
            gl.add_widget(Button(text=b, on_press=self.res))
        
        bl.add_widget(gl)
        return bl

    def res(self, instance):
        v = instance.text
        if v == "C": self.formula = "0"
        elif v == "=":
            try: self.formula = str(eval(self.formula))
            except: self.formula = "Ошибка"
        else:
            if self.formula == "0": self.formula = v
            else: self.formula += v
        self.lbl.text = self.formula

if __name__ == "__main__":
    CalcApp().run()
