from  tkinter import *
from common import *   # constants
from gui_common_mixin import *  # GUI mixin class

class LED(GUICommon):
    def __init__(self,
                 master=None,
                 width=25,
                 height=25,
                 appearance=FLAT,
                 status=STATUS_ON,
                 bd=1,
                 bg=None,
                 shape=SQUARE,
                 outline="",
                 blink=0,
                 blinkrate=1,
                 orient=POINT_UP,
                 takefocus=0
                 ):

        # assign attributes
        self.master = master
        self.shape = shape
        # self.Colors = [None, Color.OFF, Color.ON. Color.WARN, Color.ALARM, '#00ffdd']
        self.Colors = [None, OFF, ON, WARN,  ALARM, '#00ffdd']

        self.status = status
        self.blink = blink
        self.blinkrate = int(blinkrate)
        self.on = 0
        self.onState = None

        if not bg:
            bg = PANEL

        # base frame to contain light
        self.frame = Frame(master, relief=appearance, bg=bg, bd=bd, takefocus=takefocus)
        basesize = width
        d = center = int(basesize/2)

        if self.shape == SQUARE:
            # draw a SQUARE
            self.canvas = Canvas(self.frame, height = height, width = width, bg=bg, bd=0, highlightthickness=0)
            self.light = self.canvas.create_rectangle(0,0, width, height, fill=ON)

        elif self.shape == ROUND:
            # draw a circle
            r = int((basesize-2)/2)
            self.canvas = Canvas(self.frame, width=width, height=width, highlightthickness=0, bg=bg, bd=0)

            if bd > 0:
                self.border = self.canvas.create_oval(center-r, center-r, center+r, center+r)
                r = r - bd

            self.light = self.canvas.create_oval(center-r-1, center-r-1, center+r, center+r, fill=ON, outline=outline)

        else:
            # default is an ARROW
            self.canvas = Canvas(self.frame, width=width, height=width, highlightthickness=0, bg=bg, bd=0)
            x = d
            y = d

            if orient == POINT_DOWN:
                self.light = self.canvas.create_polygon(x-d, y-d, x, y+d, x+d, y-d, x-d, y-d, outline=outline)

            elif orient == POINT_UP:
                self.light = self.canvas.create_polygon(x, y-d, x-d, y+d, x+d, y+d, x, y-d, outline=outline)

            elif orient == POINT_RIGHT:
                self.light = self.canvas.create_polygon(x-d,y-d,x+d,y,x-d,y+d,x-d,y-d, outline=outline)

            elif orient == POINT_LEFT:
                self.light = self.canvas.create_polygon(x-d, y,x+d,y+d,x+d,y-d,x-d,y,outline=outline)

        self.canvas.pack(side=TOP, fill=X, expand=NO)
        self.update()

    def update(self):
        # first blink the LED, if blink is set to ON
        if self.blink:
            if self.on:
                if not self.onState:
                    self.onState = self.status

                self.status = STATUS_OFF
                self.on = 0
            else:
                if self.onState:
                    self.status = self.onState # current ON color

                self.on = 1

        self.canvas.itemconfig(self.light, fill=self.Colors[self.status])

        self.canvas.update_idletasks()

        if self.blink:
            self.frame.after(self.blinkrate * 500, self.update)


if __name__ == "__main__":
    class TestLEDS(Frame):
        def __init__(self, parent=None):
            # list of colors and blink ON/OFF
            states = [(STATUS_OFF, 0),
                      (STATUS_ON, 0),
                      (STATUS_WARN, 0),
                      (STATUS_ALARM, 0),
                      (STATUS_SET, 0),

                      (STATUS_ON, 1),
                      (STATUS_WARN, 1),
                      (STATUS_ALARM, 1),
                      (STATUS_SET, 1)]

            # list of LED types to display, with their attributes
            leds = [(ROUND, 25, 25, FLAT, 0, None, ""),
                    (ROUND, 15, 15, RAISED, 1, None, ""),
                    (SQUARE, 20, 20, SUNKEN, 1, None, "")]

            Frame.__init__(self)  # init superclass
            self.pack()
            self.master.title('LEDs')

            # iterate for each type of LED
            for shape, w, h, app, bd, orient, outline in leds:
                frame = Frame(self, bg=PANEL)
                frame.pack(anchor=N, expand=YES, fill=X)

                # iterate for the selected states
                for state, blink in states:
                    LED(frame, shape=shape, status=state, width=w, height=h, appearance=app, orient=orient, blink=blink, bd=bd,outline=outline).frame.pack(side=LEFT, expand=YES, padx=1, pady=1)

    TestLEDS().mainloop()









