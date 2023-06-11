import time
import wrap
from wrap import sprite,sprite_text
import random
wrap.world.create_world(500,500)

platform = sprite.add("mario-items", 250, 420, "moving_platform2")
speed_platform=10

ball=sprite.add("pacman",sprite.get_x(platform),400,"dot")
sprite.set_height_proportionally(ball,15)
ball_move=False

block=[]
position_block_x=50
position_block_y=200
for g in range(3):
    for i in range(14):
        block.append(sprite.add("mario-scenery",position_block_x,position_block_y,"cloud1"))
        position_block_x+=30
    position_block_x=50
    position_block_y-=40

@wrap.on_key_always(wrap.K_a)
def go_right():
        sprite.move(platform,-speed_platform, 0)

@wrap.on_key_always(wrap.K_d)
def go_right():
        sprite.move(platform, speed_platform, 0)
@wrap.on_key_down(wrap.K_SPACE)
def start_ball():
    global ball_move
    ball_move=True

@wrap.always(10)
def game():
    if ball_move==False:
        sprite.move_to(ball,sprite.get_x(platform),400)
    else:
        sprite.move(ball,0,-3)


import wrap_py
wrap_py.app.start()