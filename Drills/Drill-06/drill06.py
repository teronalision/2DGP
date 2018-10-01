import pico2d
pico2d.open_canvas()

bg = pico2d.load_image('KPU_GROUND.png')





def draw():
    pico2d.clear_canvas()
    bg.draw(0,0)
    pico2d.update_canvas()
    pico2d.delay(1/30)


draw()


pico2d.close_canvas()
