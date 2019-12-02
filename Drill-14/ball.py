import random
import game_framework
from pico2d import *


class Ball:
    image = None

    def __init__(self):
        self.x = random.randint(50, 1837 - 50)
        self.y = random.randint(50, 1109 - 50)
        if self.image is None:
            self.image = load_image("ball41x41.png")

    def set_background(self, bg):
        self.bg = bg

    def get_bb(self):
        return (self.x - 60) - self.bg.window_left - 20, self.y - self.bg.window_bottom - 20, (self.x - 60)- self.bg.window_left + 20, self.y- self.bg.window_bottom + 20

    def update(self):
        pass
    def draw(self):
        self.image.draw(self.x - self.bg.window_left - 60, self.y - self.bg.window_bottom , 41, 41)
        draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        pass
