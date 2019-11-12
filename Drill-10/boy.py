import game_framework
from pico2d import *
from ball import Ball

import game_world

# Boy Run Speed
PIXEL_PER_METER = 10.0 / 0.1
RUN_SPEED_KMPH = 30.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class RunState:

    @staticmethod
    def enter(boy, event):
        pass

    @staticmethod
    def exit(boy, event):
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        boy.x += boy.velocity * RUN_SPEED_PPS * game_framework.frame_time
        if boy.x > 1600 - 50:
            boy.dir = -1
            boy.velocity = -1
        elif boy.x < 50:
            boy.dir = 1
            boy.velocity = 1

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw((int(boy.frame) % 5) * 182, (int((15 - boy.frame) / 5)) * 167, 182, 167, 0,
                                          '', boy.x, boy.y, 182, 167)
        else:
            boy.image.clip_composite_draw((int(boy.frame) % 5) * 182, (int((15 - boy.frame) / 5)) * 167, 182, 167, 0,
                                          'h', boy.x, boy.y, 182, 167)


next_state_table = {
    RunState: {},
}


class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 162
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 1
        self.frame = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def handle_event(self, event):
        pass
