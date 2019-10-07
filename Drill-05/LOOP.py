from pico2d import *

open_canvas()
pico2d.hide_lattice()
character = load_image('animation_sheet.png')
x = 0
frame = 0
while(True):
    while x < 800:
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x += 5
        delay(0.01)
        get_events()
    while x > 0:
        clear_canvas()
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.01)
        get_events()
close_canvas()

