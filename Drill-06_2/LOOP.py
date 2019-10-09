from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global Character_x, Character_y
    global Character_Dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
Cursor = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
Cursor_x, Cursor_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
Character_x, Character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
# hide_cursor()
Character_Dir = 0  # 0 이면 right, 1이면 left
x_points = [random.randint(100, 1100) for n in range(10)]
y_points = [random.randint(100, 900) for n in range(10)]

while running:

    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    # draw p2-p3
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[2] >= Character_x:
            Character_Dir = 1
        elif x_points[2] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[2] + (t ** 3 - t ** 2) * x_points[3]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[2] + (t ** 3 - t ** 2) * y_points[3]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[3] >= Character_x:
            Character_Dir = 1
        elif x_points[3] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[2] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[3] + (t ** 3 - t ** 2) * x_points[4]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[2] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[3] + (t ** 3 - t ** 2) * y_points[4]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[4] >= Character_x:
            Character_Dir = 1
        elif x_points[4] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[3] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[4] + (t ** 3 - t ** 2) * x_points[5]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[2] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[3] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[4] + (t ** 3 - t ** 2) * y_points[5]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[5] >= Character_x:
            Character_Dir = 1
        elif x_points[5] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[4] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[5] + (t ** 3 - t ** 2) * x_points[6]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[3] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[4] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[5] + (t ** 3 - t ** 2) * y_points[6]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[6] >= Character_x:
            Character_Dir = 1
        elif x_points[6] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[5] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[6] + (t ** 3 - t ** 2) * x_points[7]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[4] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[5] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[6] + (t ** 3 - t ** 2) * y_points[7]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[7] >= Character_x:
            Character_Dir = 1
        elif x_points[7] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[6] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[7] + (t ** 3 - t ** 2) * x_points[8]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[5] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[6] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[7] + (t ** 3 - t ** 2) * y_points[8]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[8] >= Character_x:
            Character_Dir = 1
        elif x_points[8] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[7] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[8] + (t ** 3 - t ** 2) * x_points[9]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[6] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[7] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[8] + (t ** 3 - t ** 2) * y_points[9]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[9] >= Character_x:
            Character_Dir = 1
        elif x_points[9] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[9] + (t ** 3 - t ** 2) * x_points[0]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[7] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[8] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[9] + (t ** 3 - t ** 2) * y_points[0]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[0] >= Character_x:
            Character_Dir = 1
        elif x_points[0] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[0] + (t ** 3 - t ** 2) * x_points[1]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[8] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[9] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[0] + (t ** 3 - t ** 2) * y_points[1]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()
    for i in range(0, 100, 2):
        clear_canvas()
        kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
        if x_points[1] >= Character_x:
            Character_Dir = 1
        elif x_points[1] <= Character_x:
            Character_Dir = 0
        t = i / 100
        Character_x = ((-t ** 3 + 2 * t ** 2 - t) * x_points[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * x_points[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * x_points[1] + (t ** 3 - t ** 2) * x_points[2]) / 2
        Character_y = ((-t ** 3 + 2 * t ** 2 - t) * y_points[9] + (3 * t ** 3 - 5 * t ** 2 + 2) * y_points[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * y_points[1] + (t ** 3 - t ** 2) * y_points[2]) / 2
        if Character_Dir == 1:
            character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        elif Character_Dir == 0:
            character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        frame = (frame + 1) % 8
        delay(0.01)
        update_canvas()
        handle_events()


    character.clip_draw(frame * 100, (100 - Character_Dir * 100), 100, 100, Character_x - 20, Character_y + 20)
    frame = (frame + 1) % 8
    update_canvas()
    handle_events()
    delay(0.01)

close_canvas()
