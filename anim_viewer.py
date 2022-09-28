import re
from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('HeroKnight.png')
Rcharacter = load_image('R_HeroKinght.png')
x = 50
y = 100
def cha_breath(x, y, reverse):
    frame = 0
    for a in range(35):
     clear_canvas()
     grass.draw(400, 30)
     character.clip_draw(frame * 100, 440, 100, 45, x, y, 200, 100)
     update_canvas()
     frame = (frame + 1) % 8
     delay(0.05)
     get_events()

def cha_run(x, y, reverse):
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

def cha_atk(x, y, reverse):
    frame = 0
    for a in range(48):
     clear_canvas()
     grass.draw(400, 30)
     if (reverse == False):
        if (frame < 2):
         character.clip_draw(frame * 100 + 800, 385, 100, 45, x, y, 200, 100)
        elif (frame < 12):
         character.clip_draw(frame * 100 - 200, 330, 100, 45, x, y, 200, 100)
     elif (reverse == True):
        if (frame < 2):
         Rcharacter.clip_draw(frame * 100 + 800, 385, 100, 45, x, y, 200, 100)
        elif (frame < 12):
         Rcharacter.clip_draw(frame * 100 - 200, 330, 100, 45, x, y, 200, 100)
     update_canvas()
     frame = (frame + 1) % 12
     delay(0.05)
     get_events()

def cha_rush(x, y, reverse):
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

cha_breath(x, y, False)
x = cha_run(x, y, False)
cha_atk(x, y, False)
x = cha_rush(x, y, False)
cha_breath(x, y, False)
cha_atk(x, y, True)
close_canvas()
