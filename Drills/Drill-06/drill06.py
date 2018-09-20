from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
running = True
cx, cy = KPU_WIDTH // 2, KPU_HEIGHT // 2 #캐릭터
mx, my = 0, 0 #마우스
dx, dy = 0, 0 #목적지
frame = 0
hide_cursor()


def handle_events():
    global running
    global mx, my
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')



while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, mx, my)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)
    handle_events()

close_canvas()




