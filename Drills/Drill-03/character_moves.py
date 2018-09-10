from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

time = 0
x, y = 50, 90

while 1:
    clear_canvas_now()
    grass.draw_now(400,30)

    if time < 400:
        if time < 100:
            x = x+7
        elif time < 200:
            y = y+4
        elif time < 300:
            x = x-7
        else:
            y = y-4
    elif time < 800:
        r = (800-time)/400*2*3.14
        x = 400 + 200*math.cos(r)
        y = 300 + 200*math.sin(r)
    else:
        time = 0
        x = 50
        y = 90
    
    character.draw_now(x,y)
    time = time +1
    delay(0.01)
    
close_canvas()
