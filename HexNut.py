from tkinter import *
from gui_common_mixin import *
from common import *

class HexNut(GUICommon):
    def __init__(self, master, frame=1, mount=1, outside=70, inset=8, bg=PANEL, nutbase=BRONZE, top=NUT_FLAT, takefocus=0, x=-1, y=-1):
        # points = [ '%d-r2,%d+r,%d+r2,%d+r,%d+r+2,%d,%d+r2,%d-r, %d-r2,%d-r,%d-r-2,%d,%d-r2,%d+r', '%d,%d-r-2,%d+r,%d-r2,%d+r,%d+r2,%d,%d+r+2,%d-r,%d+r2,%d-r,%d-r2,%d,%d-r-2' ]
        points = [ '%d-r2,%d+r,%d+r2,%d+r,%d+r+2,%d,%d+r2,%d-r, %d-r2,%d-r,%d-r-2,%d,%d-r2,%d+r']

        self.base = nutbase
        self.status = STATUS_OFF
        self.blink = 0
        self.set_colors()
        basesize = outside + 4

        if frame:
            self.frame = Frame(master, relief="flat", bg=bg, bd=0, highlightthickness=0, takefocus=takefocus)
            self.frame.pack(expand=0)
            self.canv = Canvas(self.frame, width=basesize, bg=bg, bd=0, height=basesize, highlightthickness=0)
        else:
            self.canv = master

        center = basesize/2
        if x >= 0:
            centerx = x
            centery = x
        else:
            centerx = centery = center

        r = outside/2

        # first draw the mount if needed
        if mount:
            self.mount = self.canv.create_oval(centerx-r, centery-r, centerx+r, centery+r, fill=self.dbase, outline=self.vdbase)

        # next draw the hexnut
        r = r - (inset/2)
        r2 = r/2

        pointlist = points[top] % (centerx,centery,centerx,centery, centerx,centery,centerx,centery, centerx,centery,centerx,centery, centerx,centery)

        setattr(self, 'hexnut', self.canv.create_polygon(pointlist, outline=self.dbase, fill=self.lbase))

        # draw the inside edge of the threads
        r = r - (inset/2)
        self.canv.create_oval(centerx-r, centery-r,
                              centerx+r, centery+r,
                              fill=self.lbase, outline=self.vdbase)

        # draw the background showing the hole
        r = r - 2
        self.canv.create_oval(centerx - r, centery - r, centerx + r, center + r, fill=bg, outline="")
        self.canv.pack(side="top", fill='x', expand='no')

class Nut(Frame, HexNut):
    def __init__(self, master, outside=70, inset=8, frame=1, mount=1, bg='gray50', nutbase=CHROME, top=NUT_FLAT):
        Frame.__init__(self)
        HexNut.__init__(self, master=master, frame=frame, mount=mount, outside=outside, inset=inset, bg=bg, nutbase=nutbase, top=top)

class TestNuts(Frame, GUICommon):
    def __init__(self, parent=None):
        Frame.__init__(self)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        metals = [CHROME]

        # define nut attributes
        nuts = [(170, 14, NUT_FLAT, 0), (70, 10, NUT_FLAT, 1)]

        # iterate for each metal type
        for metal in metals:
            mframe = Frame(self, bg="slategray2")
            mframe.pack(anchor=N, expand=YES, fill=X)

            # iterate for each of the nuts
            for outside, inset, top, mount in nuts:
                Nut(mframe, outside=outside, inset=inset, mount=mount, nutbase=metal, bg="slategray2", top=top).frame.pack(side=LEFT, expand=YES, padx=1, pady=1)


if __name__ == "__main__":
    TestNuts().mainloop()