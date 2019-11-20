import random
import game_framework
from pico2d import *


class Ball:
    image = None

    def __init__(self):
        self.x = random.randint(50, 1280 - 50)
        self.y = random.randint(50, 1024 - 50)
        if self.image is None:
            self.image = load_image("ball21x21.png")

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 21, 21)
        pass

    def handle_event(self, event):
        pass
