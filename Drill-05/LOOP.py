from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global Cursor_x, Cursor_y
    global Character_x, Character_y
    global next_x, next_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            Cursor_x, Cursor_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            next_x = event.x
            next_y = event.y

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

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    Cursor.draw(Cursor_x, Cursor_y)
    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()
