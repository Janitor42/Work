import random
import time

import wrap

from wrap import sprite

wrap.world.create_world(600, 650)
wrap.world.set_back_color(105, 110, 110)

line1 = sprite.add('pacman', 300, 200, 'dot')
sprite.set_width(line1, 600)
line2 = sprite.add('pacman', 300, 400, 'dot')
sprite.set_width(line2, 600)
line3 = sprite.add('pacman', 400, 300, 'dot')
sprite.set_height(line3, 600)
line4 = sprite.add('pacman', 200, 300, 'dot')
sprite.set_height(line4, 600)

line4 = sprite.add('pacman', 300, 600, 'dot')
sprite.set_width(line4, 600)

white = sprite.add('pacman', 0, 0, 'player3')


playes_win=0
computer_win=0
text_p=sprite.add_text('player win '+str(playes_win),100,625)
text_comp=sprite.add_text('computer win '+str(computer_win),500,625)


plase = []
plase_white = []
plase_black = []
x = 100
y = 100
row=1
numbers = 1
for i in range(3):
    for g in range(4):
        if g !=4:
            name = sprite.add('pacman', x, y, 'dot')
        list = {'name': name, 'color': 'open', 'number': numbers}
        plase.append(list)
        numbers += 1
        x += 200
    y += 200
    x = 100
    row+=1


def choice_plase_player():
    global hand,rung
    for i in plase:
        if sprite.is_collide_sprite(i['name'], white) and hand == True:
            i['color'] = 'white'
            sprite.add('pacman', sprite.get_x(i['name']), sprite.get_y(i['name']), 'player3')
            plase_white.append(i['number'])
            hand = False
            rung = 'False'
            break


def calks(gamer,plases,text,win):
    calk(3, 6, gamer,plases,text,win)
    calk(1, 2, gamer,plases,text,win)
    calk(5, 10, gamer,plases,text,win)
    calk(4, 8, gamer,plases,text,win)
    # for big tic_tac_toe
    # calk(-1, -2, gamer,plases)
    # calk(-3, -6, gamer,plases)
    # calk(-5, -10, gamer,plases)
    # calk(-4, -8, gamer,plases)


def calk(value, value2, gamer,plases,text,win):
    for i in plases:
        if i in plases:
            if i + value in plases:
                if i + value2 in plases:
                    win=win+1
                    wrap.sprite_text.set_text(text,str(gamer)+' win '+str(win))



computer_choice_value = []
computer_choice_dict=[]

sprites_computer=[]
def choice_computer():
    global rung,hand,sprites_computer
    computer_choice_value.clear()
    computer_choice_dict.clear()
    for i in plase:
        if i['color'] == 'open':
            if i['number']==4 or i['number']==8 or i['number']==12:
                continue
            else:
                dict={'number':i['number'],'name':i['name']}
                computer_choice_dict.append(dict)
                computer_choice_value.append(i['number'])
    choice_c=random.choice(computer_choice_value)
    for i in plase:
        if i['number']==choice_c:
            i['color']='black'
    for i in computer_choice_dict:
        if i['number']==choice_c:
            sprites_computer=sprite.add("mario-enemies", sprite.get_x(i['name']), sprite.get_y(i['name']), 'cloud')
            plase_black.append(i['number'])
            break
    rung = 'True'

hand = False
@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def action():
    global hand, rung
    hand = not hand

rung = random.choice(['True', 'False'])



@wrap.always(15)
def move(pos_x, pos_y):
    if rung == 'True':
        sprite.move_to(white, pos_x, pos_y)
        choice_plase_player()
        calks('Player',plase_white,text_p,playes_win)
    else:
        choice_computer()
        calks('Computer',plase_black,text_comp,computer_win)


import wrap_py

wrap_py.app.start()
