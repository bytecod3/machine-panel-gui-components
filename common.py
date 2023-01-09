from  tkinter import *

# define constants
SQUARE = 1
ROUND = 2
ARROW = 3
POINT_DOWN = 0
POINT_UP = 1
POINT_RIGHT = 2
POINT_LEFT = 3

STATUS_OFF = 1
STATUS_ON = 1
STATUS_WARN = 3
STATUS_ALARM = 4
STATUS_SET = 5

class StructClass:
    pass

Color = StructClass()

Color.PANEL = '#545454'
Color.OFF = '#656565'
Color.On = '#00FF33'
Color.WARN = '#FFCC00'
Color.ALARM = '#FF4422'

class LED:
    def __init__(self, master=None, width=25, height=25,
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

        # preserve attributes
        self.master = master
        self.shape = shape
        self.onColor = Color.ON
        self.offColor = Color.OFF
        self.alarmColor = Color.ALARM
        self.warningColor = Color.WARN
        self.specialColor = '#00ffdd'
        self.status = status
        self.blink = blink
        self.blinkrate = int(blinkrate)
        self.on = 0
        self.onState = None

        if not bg:
            bg = Color.PANEL

        # base frame to contain light
        self.frame = Frame(master, relief=appearance, bg=bg, bd=bd, takefocus=takefocus)
        basesize = width
        d = center = int(basesize/2)

        if self.shape == SQUARE:
            # draw a SQUARE
            self.canvas = Canvas(self.frame, height = height, width = width, bg=bg, bd=0, highlightthickness=0)
            self.light = self.canvas.create_rectangle(0,0, width, height, fill=Color.ON)

        elif self.shape == ROUND:
            # draw a circle
            r = int((basesize-2)/2)
            self.canvas = Canvas(self.frame, width=width, height=width, highlightthickness=0, bg=bg, bd=0)

            if bd > 0:
                self.border = self.canvas.create_oval(center-r, center-r, center+r, center+r)
                r = r - bd

            self.light = self.canvas.create_oval(center-r-1, center-r-1, center+r, center+r, fill=Color.ON, outline=outline)

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





