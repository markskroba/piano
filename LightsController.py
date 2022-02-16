import board
import neopixel

class Controller:
    DOWN = 144

    def __init__(self, num_lights, color_on, color_off ):
    # state of the lights
        self.num_lights = num_lights
        self.color_on = (255,255,255)
        self.color_off = (0,0,0)
        self.next_light = 0
        self.prev_light = 0

        # initialize the lights array, turn all lights off
        self.pixels = neopixel.NeoPixel(board.D18,
                                        self.num_lights,
                                        brightness=1,
                                        pixel_order=neopixel.RGB)
        self.pixels.fill((0,0,0))

    def changeState(self, state):
        if state == Controller.DOWN:
            self.pixels[self.next_light % self.num_lights] = self.color_on
            self.next_light+=1
        else:
            self.pixels[self.prev_light % self.num_lights] = self.color_off
            self.prev_light+=1