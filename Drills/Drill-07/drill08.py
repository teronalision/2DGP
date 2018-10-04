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


def draw():
    global frame

    pico2d.clear_canvas()
    BG.draw(400, 300)
    charicter.clip_draw(frame * 100, right * 100, 100, 100, x + 400, y + 300)

    pico2d.update_canvas()
    pico2d.delay(1 / 30)
    frame = (frame + 1) % 8


def move_sec_to_thr(p1, p2, p3, p4):
    global x, y, idx, right
    if p2[0] - p1[0] < 0:
        right = False
    else:
        right = True

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = ((-t**3 +2*t**2 -t)*p1[0] + (3*t**3 -5*t**2 +2)*p2[0] + (-3*t**3 +4*t**2 +t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 +2*t**2 -t)*p1[1] + (3*t**3 -5*t**2 +2)*p2[1] + (-3*t**3 +4*t**2 +t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw()


while True:
    move_sec_to_thr(points[n], points[n+1],points[n+2],points[n+3])

    n = (n + 1) % 20

pico2d.close_canvas()