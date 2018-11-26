from pico2d import *
import world_build_state
import game_framework
import json
import pickle


name = "RankingState"

now_time = 0.0
ranking_list = []

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

def save_rank():
    global ranking_list
    ranking_list += now_time

    with open('rank.sav', 'a') as f:
        pickle.dump(ranking_list, f)
    pass


def load_rank():

    pass


def update():
    pass

def draw():
    clear_canvas()




    update_canvas()