import random
from pico2d import *
import game_world
import game_framework


class Brick:
    image = None

    def __init__(self):
        if Brick.image == None:
            Brick.image = load_image('brick180x40.png')
        self.x, self.y = 800, 200
        self.direction = 1

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.direction * 200 * game_framework.frame_time
        if self.x > 1600 - 90:
            self.direction = -1
        elif self.x < 0 + 90:
            self.direction = 1




