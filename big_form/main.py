import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
Window.softinput_mode = 'pan'

__version__ = '0.1.0'


class MyApp(App):
    title = 'Font Test'

    def build(self):
        main = GridLayout(cols=2, row_force_default=True, row_default_height='44sp')

        for i in xrange(1, 20):
            main.add_widget(Label(text='Label %d' % i, size_hint_x=None, width='120sp'))
            main.add_widget(
                TextInput(hint_text='Text input %d' % i, size_hint_x=1, multiline=False))

        return main


if __name__ == '__main__':
    MyApp().run()
