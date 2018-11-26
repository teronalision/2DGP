from pico2d import *
import world_build_state
import game_framework
import json
import pickle


name = "RankingState"

now_time = 0.0
ranking_list = []
font = None
def enter():
    font = load_font('ENCR10B.TTF', 20)
    load_rank()
    save_rank()
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
    ranking_list += [now_time]

    with open('rank.sav', 'w') as f:
        pickle.dumps(ranking_list, f)
    pass


def load_rank():
    global ranking_list

    with open('rank.sav', 'r') as f:
        ranking_list = pickle.loads(f)
    pass


def update():
    pass

def draw():
    clear_canvas()

    if font != None:
        for score in ranking_list:
            font.draw(500,500,'(#1 %3.2r)' % score, (0,0,0))


    update_canvas()