from pico2d import *
open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
right = True


def move_to(dx, dy): #목표로
    global x, y, right
    cx, cy = x, y
    if dx - cx > 0:
        right = True
    else:
        right = False
        
    i = 0
    while i <30 :
        x += (dx -cx)/30
        y += (dy -cy)/30
        i+=1
        cDraw()
        

def cDraw(): #그리기
    global frame
    clear_canvas()
    character.clip_draw(frame//3*100 ,right*100 ,100 ,100 ,x ,y)
    update_canvas()
    delay(1/30)
    frame = (frame +1) %24


#메인
while True:
    for ix, iy in  [(203, 535),(132, 243),(535, 470),(477, 203),(715, 136),(316, 225),(510, 92),(692, 518),(682, 336),(712, 349)]:
        move_to(ix, iy)
    
    
close_canvas()
