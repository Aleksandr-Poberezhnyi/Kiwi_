from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
 
# import instraction
 
name = ''
age = 7
p1, p2, p3 = 0, 0, 0
 
class Window1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = Label(text = "Следуй инструкциям)", color =(0.5, 0.5, 0.5, 1))
        self.mainLayout = BoxLayout(orientation = 'vertical')
        self.nameLayout = BoxLayout()
        self.ageLayout = BoxLayout()
        self.textName = Label(text = 'Введите имя:')
        self.textAge = Label(text = 'Введите возраст:')
        self.inputName = TextInput()
        self.inputAge = TextInput()
        self.nameLayout.add_widget(self.textName)
        self.nameLayout.add_widget(self.inputName)
        self.ageLayout.add_widget(self.textAge)
        self.ageLayout.add_widget(self.inputAge)
 
        self.button = Button(text = 'Начать')
        self.button.on_press = self.trigger
 
        self.mainLayout.add_widget(self.text)
        self.mainLayout.add_widget(self.nameLayout)
        self.mainLayout.add_widget(self.ageLayout)
        self.mainLayout.add_widget(self.button)
 
        self.add_widget(self.mainLayout)
        
    def trigger(self):
        global name
        global age 
        name = self.inputName.text
        age = self.inputAge.text
        age = self.checkpoint(age)
        if age:
            if age > 6:
                self.manager.current = '...'
            else:
                self.textAge.text = "Введите число больше 6-ти"  
        
    def checkpoint(self, value):
        try:
            value = int(value)
            return value
        except:
            self.textAge.text = "Введите число"
            return False
        
 
class Ruffie(App):
    def build(self):
        build = ScreenManager()
        build.add_widget(Window1(name = 'Anton'))
        return build
 
 
app = Ruffie()
app.run()



