from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MainWindow(BoxLayout):
    # self.ids.input.text = '0'
    def clear(self):
        self.ids.textinput.text = ""

    def button_press(self, button):

        text = self.ids.textinput.text
        if text == "":
            self.ids.textinput.text = f"{button}"
        else:
            self.ids.textinput.text = f"{text}{button}"

    def evaluate(self):
        calculation = str(self.ids.textinput.text)
        self.ids.textinput.text = str(eval(calculation))

    def backspace(self):
        self.ids.textinput.text = self.ids.textinput.text[:-1]
        # print(back)

    def ce(self):
         self.ids.textinput.text = "0"

    def percentage(self):
        self.ids.textinput.text = str(int(eval(str(self.ids.textinput.text)))/100)
        # print(per)


class CalculatorApp(App):
    pass

if __name__ == '__main__':
    CalculatorApp().run()