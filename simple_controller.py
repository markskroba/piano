# libraries for controlling lights
import board
import neopixel
from LightsController import Controller

class SimpleController(Controller):
    DOWN = 144

    def __init__(self, num_lights, color_on, color_off):
        # state of the lights
        super.__init__(num_lights, color_on, color_off)


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)

        changeState(self, state)

#        if state == SimpleController.DOWN:
#            self.pixels[self.next_light % self.num_lights] = self.color_on
#            self.next_light+=1
#        else:
#           self.pixels[self.prev_light % self.num_lights] = self.color_off
#            self.prev_light+=1
