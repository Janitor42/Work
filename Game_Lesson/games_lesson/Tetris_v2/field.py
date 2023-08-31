import random
import time
import wrap
from wrap import sprite, sprite_text, world
import figure as mod_figure

Remove = False


class Field():
    def __init__(self):
        self.fields = []
        self.work_fields = []
        self.work_fields_new = []

        y_y = 590
        x_x = 20
        numbers = 1
        height = 1
        for y in range(21):
            for x in range(11):
                if x != 11:
                    dici = {'x': x_x, 'y': y_y, 'state': False, 'number': numbers, 'height': height}
                    x_x += 30
                    self.fields.append(dici)
                numbers += 1
                x += 200
            y_y -= 30
            x_x = 20
            height += 1
        print(self.fields)

    def remove_and_add_work_field(self):
        global Remove, move_row, remove_row

        for i in self.fields:
            if i['state'] == True:
                name = sprite.add('pacman', i['x'], i['y'])
                sprite.set_size(name, 28, 28)
                listik = [i['x'], i['y']]
                dici = {'name': name, 'height': i['height'], "pos": listik}
                self.work_fields.append(dici)
                i['state'] = False

        len_row = 0
        for value in range(1, 21):
            for name in self.work_fields:
                if name['height'] == value:
                    len_row += 1
                    if len_row == 10:
                        remove_row(self.work_fields, value, self.work_fields_new)
                        move_row(self.work_fields, value)
            len_row = 0

            def remove_row(work_field, value, work_field_new):
                for i in work_field:
                    if i['height'] == value:
                        sprite.hide(i['name'])

                work_field_new.clear()
                for i in work_field:
                    if i['height'] != value:
                        work_field_new.append(i)
                work_field.clear()
                work_field += work_field_new

            def move_row(work_field, value):
                for i in work_field:
                    if i['height'] > value:
                        sprite.move(i['name'], 0, 30)
                        i['height'] = i['height'] - 1

    def add_field(self, figure:mod_figure.Figure):
        if not figure.check:
            return
        for dot in self.fields:
            if collide_dot(dot, figure.names):
                dot['state'] = True


def collide_dot(dot, names):
    for name in names:
        if sprite.is_collide_point(name, dot['x'], dot['y']):
            return True
    return False
