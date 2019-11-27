import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import boy

import world_build_state

name = "MainState"


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

zombie = None
boy = None
font = None
score = None
ranks = {"#1": 1.0, "#2": 1.0, "#3": 1.0, "#4": 1.0,
         "#5": 1.0, "#6": 1.0, "#7": 1.0, "#8": 1.0,
         "#9": 1.0, "#10": 1.0}
def enter():
    global boy
    global font, score, ranks
    boy = world_build_state.get_boy()
    font = load_font('ENCR10B.TTF', 20)

    score = get_time() - boy.start_time
    with open('ranks.json', 'w') as f:
        json.dumps(ranks, f)




    pass

def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass


def draw():
    global boy
    global font, score
    clear_canvas()
    font.draw(600, 500, 'Score: %3.2f' % score, (0, 0, 0))
    update_canvas()






