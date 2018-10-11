import game_framework
import main_state
from pico2d import *


name = "PauseState"
image = None
time = 0

def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image,time
    del(image)
    time = 0


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()


def draw():
    clear_canvas()
    main_state.grass.draw()
    main_state.boy.draw()

    if time % 10 < 5:
        image.draw(400, 300,300,300)
    update_canvas()


def update():
    global time
    time +=1
    handle_events()
    delay(0.2)
