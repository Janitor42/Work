import wrap
import time
import random
from wrap import sprite
from random import randint, choice, randrange

def create():
    global l,h
    h=randrange(98,603,83)
    l=400
    id = sprite.add("mario-enemies", l, h, 'cloud')
    # id2 = wrap.sprite.add_text(str(hp), wrap.sprite.get_x(id), wrap.sprite.get_y(id), bold=True, font_size=15)
    a={"Name": id,  "HP": 1000, "speed ": 3}
    return a


def move_to_sprite(player,enemie,friend):
    global a,angle
    x=sprite.get_x(enemie["Name"])
    y=sprite.get_y(enemie["Name"])
    sprite.move_at_angle_point(enemie["Name"], sprite.get_x(player), sprite.get_y(player),3)
    for i in friend:
        if i is enemie:
            continue
        if sprite.is_collide_sprite(enemie["Name"],i["Name"]):
            sprite.move_at_angle_point(enemie["Name"],random.randint(-500,500),random.randint(-500,500),6)
    sprite.move_to(enemie["Name_text"], sprite.get_x(enemie["Name"]), sprite.get_y(enemie["Name"]))

    for i in friend:
        if i is enemie:
            continue
        if sprite.is_collide_sprite(enemie["Name"],i["Name"]):
            sprite.move_at_angle_point(enemie["Name"],x,y,10)
    sprite.move_to(enemie["Name_text"], sprite.get_x(enemie["Name"]), sprite.get_y(enemie["Name"]))