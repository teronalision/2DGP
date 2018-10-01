import pico2d
import random
pico2d.open_canvas()

BG = pico2d.load_image('KPU_GROUND.png')
charicter = pico2d.load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
right = True

points = [(random.randint(-300,-300),random.randint(-300,-300)) for n in range(20)]
idx = 0

def draw():
    pico2d.clear_canvas()
    BG.draw(400,300)
    charicter.clip_draw(frame*100,right*100,100,100,x,y)
    
    pico2d.update_canvas()
    pico2d.delay(1/30)

def move():
    global x, y, idx
    x, y = points[idx]
    idx = (idx+1)%20

while True:
    
    draw()
    frame=(frame+1) %8

pico2d.close_canvas()
