from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_shet.png')

point = ((203, 535),(132, 243),(535, 470),(477,203),(715, 136),(316, 225),(510, 92),(692, 518),(682, 336),(712, 349))
x, y = 800 //2, 600 //2
frame = 0
right = True


def move_to((dx, dy)):
    while !(x == dx && y == dy):
        cDraw()

def cDraw():
    clear_canvas()
    character.clip_draw(frame*100 ,right*100 ,100 ,100 ,x ,y)
    update_canvas()

#메인
while True:
    for dst in point:
        move_to(dst)
    
    
close_canvas()
