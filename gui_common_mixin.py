from common import *

"""
use the LED class as  Mixin class
"""
class GUICommon:
    def turnon(self):
        self.status = STATUS_ON
        if not self.blink: self.update()

    def turnoff(self):
        self.status = STATUS_OFF
        if not self.blink: self.update()

    def alarm(self):
        self.status = STATUS_ALARM
        if not self.blink: self.update()

    def warn(self):
        self.status = STATUS_WARN
        if not self.blink: self.update()

    def set(self, color):
        self.status = STATUS_SET
        self.specialColor = color
        self.update()

    def blinkon(self):
        if not self.blink:
            self.blink = 1
            self.onState = self.status
            self.update()

    def blinkoff(self):
        if self.blink:
            self.blink = 0
            self.status = self.onState
            self.onState = None
            self.on = 0
            self.update()

    def blinkstate(self, blinkstate):
        if blinkstate:
            self.blinkon()
        else:
            self.blinkoff()

    def update(self):
        raise NotImplementedError

    def transform(self, rgb, factor):
        retval = '#'
        for v in [rgb[0], rgb[1], rgb[2]]:
            v = int((v * factor )/256)
            if v > 255: v = 255
            if v < 0: v = 0
            retval = "%s%02x" % (retval, v)

        return retval

    def set_colors(self):
        '''
        This function factors dark, very dark, light and very light colors
        '''
        rgb = self.winfo_rgb(self.base)
        self.dbase = self.transform(rgb, 0.8)
        self.vdbase = self.transform(rgb, 0.7)
        self.lbase = self.transform(rgb, 1.1)
        self.vlbase = self.transform(rgb, 1.3)






