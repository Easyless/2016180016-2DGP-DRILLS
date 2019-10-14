from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    pass


class Boy:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    pass


class Ball:

    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 599
        self.type = random.randint(0, 1)
        self.speed = random.randint(5,15)
        self.smallimage = load_image('ball21x21.png')
        self.bigimage = load_image('ball41x41.png')

    def drop(self):
        if self.y > 90 - (21 + (self.type * 20)):
            self.y -= self.speed

    def draw(self):
        if self.type == 0:
            self.smallimage.draw(self.x, self.y, 21, 21)
        elif self.type == 1:
            self.bigimage.draw(self.x, self.y, 41, 41)
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

team = [Boy() for i in range(11)]
balls = [Ball() for i in range(20)]
grass = Grass()

running = True

while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.drop()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.05)

close_canvas()
