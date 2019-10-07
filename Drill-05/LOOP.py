from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running, Move
    global Cursor_x, Cursor_y
    global Character_x, Character_y
    global next_x, next_y
    global start_x , start_y
    global Character_Dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            Cursor_x, Cursor_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN and event.button == SDL_BUTTON_LEFT:
            if Character_x <= Cursor_x:
                Character_Dir = 0
            elif Character_x >= Cursor_x:
                Character_Dir = 1
            start_x = Character_x
            start_y = Character_y
            next_x = event.x
            next_y = event.y
            Move = True

        pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
Cursor = load_image('hand_arrow.png')
character = load_image('animation_sheet.png')

running = True
Cursor_x, Cursor_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
Character_x, Character_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
Character_Dir = 0 # 0 이면 left, 1이면 right
Move = False
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    if Character_Dir == 0:
        character.clip_draw(frame * 100, 100, 100, 100, Character_x, Character_y)
        if Move == True:
            for i in range(0, 100 + 1, 2):
                t = i / 100
                Character_x = (1-t)*start_x+t*next_x
                Character_x = (1-t)*start_y+t*next_y
                delay(0.01)
        Move = False

    elif Character_Dir == 1:
        character.clip_draw(frame * 100, 0, 100, 100, Character_x, Character_y)
        if Move == True:
            for i in range(0, 100 + 1, 2):
                t = i / 100
                Character_x = (1-t)*start_x+t*next_x
                Character_x = (1-t)*start_y+t*next_y
                delay(0.01)
        Move = False



    Cursor.draw(Cursor_x, Cursor_y)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

close_canvas()
