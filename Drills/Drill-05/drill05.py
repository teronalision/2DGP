from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y = 0, 0
frame = 0
right = True


def move_to(dx, dy): #목표로
    cx, cy = x, y
    while x != dx:
        x += (dx -cx)//30
        y += (dy -cy)//30
        
        cDraw()
        

def cDraw(): #그리기
    clear_canvas()
    character.clip_draw(frame*100 ,right*100 ,100 ,100 ,x ,y)
    update_canvas()


#메인
while True:
    for ix, iy in  (203, 535):
        move_to(ix, iy)
    
    
close_canvas()
