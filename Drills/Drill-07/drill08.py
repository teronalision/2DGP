import pico2d
import random

pico2d.open_canvas()

BG = pico2d.load_image('KPU_GROUND.png')
charicter = pico2d.load_image('animation_sheet.png')

x, y = 400, 300
frame = 0
right = True
n = 0

points = [(random.randint(-200, 200), random.randint(-200, 200)) for n in range(10)]
#points = [(0,0),(800,100),(600,200),(400,600)]


def draw():
    global frame

    pico2d.clear_canvas()
    BG.draw(400, 300)
    charicter.clip_draw(frame//3 * 100, right * 100, 100, 100, x + 400, y + 300)

    pico2d.update_canvas()
    pico2d.delay(1 / 30)
    frame = (frame + 1) % 24


def move_sec_to_thr(p1, p2, p3, p4):
    global x, y, idx, right
    if p3[0] - p2[0] < 0:
        right = False
    else:
        right = True


    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = ((-t**3 +2*t**2 -t)*p1[0] + (3*t**3 -5*t**2 +2)*p2[0] + (-3*t**3 +4*t**2 +t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 +2*t**2 -t)*p1[1] + (3*t**3 -5*t**2 +2)*p2[1] + (-3*t**3 +4*t**2 +t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw()


while True:
    n1 = n
    n2 = (n1+1)%10
    n3 = (n2+1)%10
    n4 = (n3+1)%10
    
    move_sec_to_thr(points[n1], points[n2],points[n3],points[n4])

    n = (n + 1) % 10

pico2d.close_canvas()
