import pico2d
pico2d.open_canvas()

BG = pico2d.load_image('KPU_GROUND.png')
charicter = pico2d.load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
right = True

def draw():
    pico2d.clear_canvas()
    BG.draw(400,300)
    charicter.clip_draw(frame*100,right*100,100,100,x,y)
    
    pico2d.update_canvas()
    pico2d.delay(1/30)




while True:
    draw()

pico2d.close_canvas()
