from tkinter import *
from gui_common_mixin import *

import string

class TestColors(Frame, GUICommon):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.base = '#848484'
        self.pack()
        self.set_colors()
        self.make_widgets()

    def make_widgets(self):
        for tag in ["VDBase", "DBase", "LBase", "VLBase"]:
            Button(self, text=tag, bg=getattr(self, '%s' % tag.lower()), fg='white', command=self.quit).pack(side=LEFT)

if __name__ == '__main__':
    TestColors().mainloop()
