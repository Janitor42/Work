import wrap
from wrap import sprite
import random
wrap.world.create_world(500,500)
wrap.world.set_back_color(137, 193, 204)

#Препядствие игрока

let_1={}
let_2={}
def add_blocks(let,x):
    block_up = random.randint(20, 350)
    for i in range(-50,block_up,30):
        let[i]=sprite.add("mario-items", x, i, "block_empty")
    for i in range(block_up+150,550,30):
        let[i]=sprite.add("mario-items", x, i, "block_empty")

add_blocks(let_1,1000)
add_blocks(let_2,1350)


#Создание списков(трубы и песок) и размещение их на экране
imitation_line= {}
imitation_block={}
x_pos_imitation_line=0
for i in range(7):
    imitation_line[i]=sprite.add("mario-items",x_pos_imitation_line, 450, "moving_platform2")
    imitation_block[i]=sprite.add("battle_city_items",x_pos_imitation_line,480,"block_snow")
    sprite.set_width(imitation_line[i],100)
    sprite.set_width(imitation_block[i],100)
    sprite.set_height(imitation_block[i],50)
    x_pos_imitation_line=x_pos_imitation_line+100

#Игрок
player = sprite.add("mario-1-big",250,250,"duck")
player_on_game=False
pos_x_player=1
angle_mario=-3
angle_triger=True


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def start_game():
    global player_on_game,angle_triger
    sprite.move(player,0,-50)
    player_on_game = True
    angle_triger=True

#Угол персонажа во время нажатия мышки
def change_angle():
    global angle_triger
    if sprite.get_angle(player) > 45 and angle_triger==True:
        sprite.set_angle(player, 45)
        if sprite.get_angle(player)<50:
            angle_triger=False
    elif sprite.get_angle(player)<180:
        sprite.set_angle(player, sprite.get_angle(player)+abs(angle_mario))

#функция проверяет блок за экраном и ставит его в конец экрана, работает с 2 видами блоков
def return_pos(return_elements,x):
    if sprite.get_x(return_elements) < -100:
        sprite.move_to(return_elements, 590, x)


#Работа с движением удалением и новыми let
def actions_let(let,y_pos):
    for i in let:
        sprite.move(let[i],-3,0)
        if sprite.get_x(let[i])<0:
            hide_sprite(let)
            let.clear()
            break
    if let=={}:
        add_blocks(let, y_pos)
def hide_sprite(let):
    for i in let:
        sprite.hide(let[i])

@wrap.always(50)
#Имитация скорости движения по экрану
def imitation_moution():
    for i in imitation_line:
        sprite.move(imitation_line[i],-10,0)
        sprite.move(imitation_block[i], -10, 0)
        return_pos(imitation_line[i],450)
        return_pos(imitation_block[i],480)

@wrap.always(35)
#Движение персонажа в игре
def game():
    global pos_x_player,player_on_game
    global let_1, let_2
    if player_on_game==False:
        sprite.move(player,0,pos_x_player)
        if sprite.get_y(player)>260:
            pos_x_player=-pos_x_player
        if sprite.get_y(player) < 240:
            pos_x_player=-pos_x_player
    else:
        sprite.move(player,0,5)
        change_angle()
        actions_let(let_1, 650)
        actions_let(let_2, 650)

@wrap.always(25)
def game():
#Поворот персонажа в игре
    global player_on_game
    if player_on_game==True:
        change_angle()


import wrap_py
wrap_py.app.start()