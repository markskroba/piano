# libraries for controlling lights
import board
import neopixel
import LightsController

class SimpleController(LightsController.Controller):
    DOWN = 144

    def __init__(self, num_lights, color_on, color_off):
        # state of the lights
        super.__init__(num_lights, color_on, color_off)


    def process_event(self, event):
        message, deltatime = event
        state = message[0]
        print(message, deltatime)

