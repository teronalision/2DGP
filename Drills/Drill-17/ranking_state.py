from pico2d import *
import world_build_state
import game_framework


name = "RankingState"

now_time = 0.0


def enter():
    pass

def exit():
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
    clear_canvas()




    update_canvas()