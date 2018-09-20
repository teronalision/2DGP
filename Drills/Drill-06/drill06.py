from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2 #캐릭터
mx, my = 0, 0 #마우스
dx, dy = x, y #목적지
frame = 0
hide_cursor()
dir = 0

def move_to(dx, dy): #목표로
    global x, y
    global dir
    
    a = dx - x
    b = dy - y

    if abs(a) > 10:
        a /= 2
    if abs(b) > 10:
        b /= 2

    x = x + a/10
    y = y + b/10

    if dx > x:
        dir = 1
    elif dx == x:
        dir = 0
    else:
        dir = -1

def handle_events():
    global running
    global mx, my
    global dx, dy
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            dx, dy = event.x -25, KPU_HEIGHT +25 - event.y
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand.draw(mx,my)
    if dir == 1:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        frame = (frame + 1) % 8
    elif dir == -1:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        frame = (frame + 1) % 8  
    else:
        character.clip_draw(0,300,100,100,x,y)

    move_to(dx,dy)
    update_canvas()
    delay(0.02)
    handle_events()

close_canvas()




