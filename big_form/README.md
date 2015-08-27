Big Form
========

This program shows how to prevent the virtual keyboard from covering up your text inputs. The key is this snippet:

```python
from kivy.core.window import Window
Window.softinput_mode = 'pan'
```

Source: http://stackoverflow.com/questions/26799084/android-on-screen-keyboard-hiding-python-kivy-textinputs