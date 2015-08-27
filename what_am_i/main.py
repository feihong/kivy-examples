import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty


__version__ = '0.1.0'


Builder.load_string("""
<Main>:
    orientation: 'vertical'
    answer_textinput: answer

    Label: 
        size_hint: 1, None
        text: 'What am I?'
        font_size: sp(32)
    Image:
        size_hint: 1, 1
        # size: 720, 511        
        source: 'asian_palm_civet.jpg'        
    BoxLayout:
        size_hint: 1, None
        TextInput:
            id: answer
            hint_text: 'Enter your answer here'
            multiline: False
            size_hint: 1, None
            on_text_validate: root.submit()
        Button:
            text: 'Submit'
            size_hint: None, None
            width: sp(100)
            on_press: root.submit()
    BoxLayout:
        size_hint: 1, None
        Button:
            text: 'Hint 1'
            on_press: root.show_hint('You can use Google')
        Button:
            text: 'Hint 2'
            on_press: root.show_hint('I can be used to make coffee')
    Widget:
        size_hint: 1, 1

<Widget>:
    font_size: sp(16)
""")


class Main(BoxLayout):
    answer_textinput = ObjectProperty(None)

    def show_hint(self, text):
        show_message(text)

    def submit(self):
        answer = self.answer_textinput.text.strip().lower()
        if answer == 'mammal':
            show_message('Yeah, but what kind of mammal?')
        elif answer == 'civet':
            show_message('You are awesome!')
        else:
            show_message('Please try again')

        print self.answer_textinput.font_name


def show_message(text):
    popup = Popup(
        title=u'\u4f60\u597d', 
        content=Label(text=text),
        size_hint=(.9, .5))
    popup.open()

class MyApp(App):
    title = 'What Am I?'

    def build(self):
        return Main()

if __name__ == '__main__':
    MyApp().run()
