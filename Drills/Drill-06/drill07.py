import pico2d
import random
pico2d.open_canvas()

BG = pico2d.load_image('KPU_GROUND.png')
charicter = pico2d.load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
right = True
n = 1

points = [(random.randint(-200,200),random.randint(-200,200)) for n in range(20)]

def draw():
    global frame

    
    pico2d.clear_canvas()
    BG.draw(400,300)
    charicter.clip_draw(frame*100,right*100,100,100,x+400,y+300)
    
    pico2d.update_canvas()
    pico2d.delay(1/30)
    frame=(frame+1) %8

def move(p1,p2):
    global x, y, idx, right
    if p2[0] - p1[0] < 0:
        right = False
    else:
        right = True
    
    for i in range(0, 100 +1, 4):
        t = i /100
        x = (1-t)*p1[0] +t*p2[0]
        y = (1-t)*p1[1] +t*p2[1]
        draw()
        

while True:
    
    move(points[n-1],points[n])
    
    n = (n+1) %20

pico2d.close_canvas()
