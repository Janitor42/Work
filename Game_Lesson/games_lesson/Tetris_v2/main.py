import random
import time
import wrap
from wrap import sprite,sprite_text,world
import menu
import figure
import field


world.create_world(800,612)
menu.create_border()

this=figure.Figure(1)
they=field.Field()


@wrap.on_key_down(wrap.K_w)
def turn():
    this.Turn(they.work_fields)

@wrap.on_key_down(wrap.K_a)
def left():
    this.left(they.work_fields)
@wrap.on_key_down(wrap.K_d)
def right():
    this.right(they.work_fields)
@wrap.on_key_down(wrap.K_s)
def down():
    this.down()
print(they.fields)
@wrap.always(50)
def game():
    this.move_figure(they.work_fields)
    they.add_field(this)
    this.remove_figure_and_add_up()
    they.remove_and_add_work_field()




import wrap_py
wrap_py.app.start()
