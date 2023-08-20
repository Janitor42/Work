import random
import time
import wrap
from wrap import sprite,sprite_text,world
import menu
import object
import field


world.create_world(800,600)
menu.create_border()

this=object.Figure(1)
they=field.Field()


@wrap.on_key_down(wrap.K_w)
def turn():
    this.Turn()
@wrap.on_key_down(wrap.K_a)
def left():
    this.left()
@wrap.on_key_down(wrap.K_d)
def right():
    this.right()
@wrap.on_key_down(wrap.K_s)
def down():
    this.down()

@wrap.always(50)
def game():
    this.work_platform(they.work_fields)
    they.Add_field(this.names)
    this.remove_names()
    they.Add_work_field()






import wrap_py
wrap_py.app.start()
