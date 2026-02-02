































from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=5)
        
        # Экран вывода
        self.solution = Label(text="0", font_size=50, halign="right", 
                              valign="middle", size_hint=(1, 0.4))
        self.solution.bind(size=self.solution.setter('text_size'))
        main_layout.add_widget(self.solution)
        
        # Сетка кнопок
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
        grid_layout = GridLayout(cols=4, spacing=5)
        for row in buttons:
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
