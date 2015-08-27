import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

__version__ = '0.1.0'

Builder.load_file('main.kv')


class Main(BoxLayout):
    text_input = ObjectProperty()
    data_label = ObjectProperty()

    def update_data(self):
        self.data_label.text = u'Font: %s\nChinese text: %s' % (
            self.text_input.font_name,
            u'\u4f60\u597d')

class MyApp(App):
    title = 'Font Test'

    def build(self):
        return Main()

if __name__ == '__main__':
    MyApp().run()
