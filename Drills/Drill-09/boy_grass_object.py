from pico2d import *


# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
running = True
open_canvas()

boy = Boy()
grass = Grass()

# game main loop code

while running:
    handle_events()
    delay(1)
close_canvas()

# finalization code