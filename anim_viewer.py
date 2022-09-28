import re
from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('HeroKnight.png')
x = 50
y = 100

def cha_breath(x, y):
    frame = 0
    for a in range(16):
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 100, 440, 100, 45, x, y, 200, 100)
     update_canvas()
     frame = (frame + 1) % 8
     delay(0.05)
     get_events()

def cha_run(x, y):
    frame = 0
    while (x < 400):
        clear_canvas()
        grass.draw(400,30)
        if (frame < 2):
         character.clip_draw(frame * 100 + 800, 440, 100, 45, x, y, 200, 100)
        elif (frame >= 2):
         character.clip_draw(frame * 100 - 200, 385, 100, 45, x, y, 200, 100)
        update_canvas()
        frame = (frame + 1) % 10
        x = x + 15
        delay(0.05)
        get_events()
    return x

def cha_atk(x, y):
    frame = 0
    for a in range(12):
     clear_canvas()
     grass.draw(400, 30)
     if (frame < 2):
         character.clip_draw(frame * 100 + 800, 385, 100, 45, x, y, 200, 100)
     elif (frame < 12):
         character.clip_draw(frame * 100 - 200, 330, 100, 45, x, y, 200, 100)
     update_canvas()
     frame = (frame + 1) % 12
     delay(0.05)
     get_events()

def cha_rush(x, y):
    frame = 0
    for a in range(9):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame * 100 + 100, 55, 100, 45, x, y, 200, 100)
        update_canvas()
        frame = (frame + 1) % 9
        x = x + 25
        delay(0.05)
        get_events()
    return x

def cha_jump(x, y):
    frame = 0
    for a in range(8):
        clear_canvas()
        grass.draw(400, 30)
        if (frame < 3):
            character.clip_draw(frame * 100 + 700, 275, 100, 45, x, y, 200, 100)
            y = y + 50
        elif (frame < 8):
            character.clip_draw(frame * 100 - 300, 220, 100, 45, x, y, 200, 100)
            y = y - 30
        update_canvas()
        frame = (frame + 1) % 8
        delay(0.05)
        get_events()

cha_breath(x, y)
cha_jump(x, y)
cha_breath(x, y)
x = cha_run(x, y)
cha_breath(x, y)
cha_atk(x, y)
cha_breath(x, y)
cha_atk(x, y)
cha_atk(x, y)
cha_breath(x, y)
x = cha_rush(x, y)
cha_breath(x, y)
cha_jump(x, y)
cha_jump(x, y)
cha_breath(x, y)

close_canvas()
