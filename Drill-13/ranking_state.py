import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world
import boy

import world_build_state

name = "ranking_State"


def collide(a, b):
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
data = []


def load_data():
    global data, score

    with open('temp.json', 'r') as f:
        data = json.load(f)
    data.append(score)
    data.sort(reverse=True)


def save_data():
    global data
    del data[-1]
    with open('temp.json', 'w') as f:
        json.dump(data, f)


def enter():
    global boy, font, score, data

    boy = world_build_state.get_boy()
    font = load_font('ENCR10B.TTF', 20)
    score = get_time() - boy.start_time
    load_data()
    print(data)
    save_data()

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
    global boy, font, score
    clear_canvas()
    font.draw(600, 800, 'Ranking')
    counter = 9
    while counter != -1:
        font.draw(600, 700 - counter * 30, '#' + str(counter) + ': ' + str(data[counter]), (0, 0, 0))
        counter -= 1

    update_canvas()
