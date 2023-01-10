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

