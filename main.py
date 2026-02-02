
















































from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

# 1. Создаем основной контейнер интерфейса
root = BoxLayout(orientation='vertical', padding=5)

# 2. Экран вывода цифр
display = Label(text='0', size_hint_y=0.2, font_size='40sp')
root.add_widget(display)

# 3. Сетка для кнопок (4 колонки)
grid = GridLayout(cols=4, spacing=5)

def on_press(instance):
    if instance.text == 'C':
        display.text = '0'
    elif instance.text == '=':
        try:
            # Математическое вычисление введенной строки
            display.text = str(eval(display.text))
        except:
            display.text = 'Ошибка'
    else:
        if display.text == '0' or display.text == 'Ошибка':
            display.text = instance.text
        else:
            display.text += instance.text

# 4. Список кнопок в нужном порядке
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for btn_text in buttons:
    btn = Button(text=btn_text, font_size='30sp')
    btn.bind(on_release=on_press)
    grid.add_widget(btn)

root.add_widget(grid)

# 5. Запуск во всплывающем окне для удобства теста
popup = Popup(title='Мой Калькулятор', content=root, size_hint=(0.95, 0.95))
popup.open()
