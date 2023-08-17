import random
import time
import wrap
from wrap import sprite, sprite_text, world
import object

qw=None
wq2=None
class Field():
    def __init__(self):
        self.fields = []
        self.work_fields = []
        self.work_names=[]
        self.name = 0
        self.dici = {}
        y_y = 590
        x_x = 20
        numbers = 1
        for y in range(21):
            for x in range(11):
                if x != 11:
                    self.name = sprite.add('pacman', x_x, y_y, 'dot')
                    sprite.set_size(self.name,0.1,0.1)
                    x_x += 30
                self.dici = {'name': self.name, 'state': False, 'number': numbers}
                self.fields.append(self.dici)
                numbers += 1
                x += 200
            y_y -= 30
            x_x = 20

    def Add_field(self, names):
        if object.check:
            for k in self.fields:
                if sprite.is_collide_any_sprite(k['name'], names):
                    k['state'] = True
                    sprite.set_size(k['name'], 20, 20)

    def Remove_field(self):
        global qw,qw2
        for i in self.fields:
            if i['state'] == True:
                self.work_fields.append(i['number'])
                self.work_names.append(i['name'])
                i['state']=False
        for i in self.work_fields:
            if i + 1 in self.work_fields and i + 2 in self.work_fields and i + 3 in self.work_fields and i + 4 in self.work_fields and i + 5 in self.work_fields and i + 6 in self.work_fields \
and i + 6 in self.work_fields and i + 7 in self.work_fields and i + 8 in self.work_fields and i + 9 in self.work_fields:
                qw=i
                qw2=i
                for y in self.fields:
                    if y['number'] == qw:
                        sprite.set_size(y['name'], 30, 30)
                        qw+=1
                        if 10+qw2 <= qw:
                            break




