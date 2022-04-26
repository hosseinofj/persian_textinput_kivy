# you must have tow library named python_bidi and arabic_reshper

import arabic_reshaper
from bidi.algorithm import get_display

# Importing Kivy related libraries
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.properties import (
                            StringProperty,
                            NumericProperty
                            )

# KV section

KV = '''
<Fa_text@TextInput>:
    text: "efevresi.com"
    multiline: 0
    font_name: "data/Lalezar-Regular.ttf" # the font you want to use
    font_size: 26
    padding_y: [6,0] # can be changed
    padding_x: [self.size[0]-self._get_text_width(max(self._lines, key=len), self.tab_width, self._label_cached)-10,8]
'''


# Python Section

class Fa_text(TextInput):
    max_chars = NumericProperty(20) # maximum character allowed
    str = StringProperty()

    def insert_text(self, substring, from_undo=False):
        if not from_undo and (len(self.text) + len(substring) > self.max_chars):
            return
        self.str = self.str+substring
        self.text = get_display(arabic_reshaper.reshape(self.str))
        substring = ""
        super(Fa_text, self).insert_text(substring, from_undo)

    def do_backspace(self, from_undo=False, mode='bkspc'):
        self.str = self.str[0:len(self.str)-1]
        self.text = get_display(arabic_reshaper.reshape(self.str))
        
class TestApp(App):
    def build(self):
        self.count = 0
        Builder.load_string(KV)
        return Fa_text()
        
if __name__ == '__main__':
    TestApp().run()
