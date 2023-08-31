import random
import time
import wrap
from wrap import sprite, sprite_text, world
import menu

log_turn = True
danger = False


def create_figure(names, this_figure):
    if this_figure == 1:
        x = 110
        y = 0
        for i in range(4):
            names.append(sprite.add('pacman', x, y, 'dot'))
            sprite.set_size(names[-1], 28, 28)
            x += 30


class Figure:
    def __init__(self, this_figure):
        self.check = False
        self.names = []
        self.this_figure = this_figure
        self.turn = False
        self.calk_pos = []
        create_figure(self.names, this_figure)

    def move_figure(self, they):
        self.check = self._touch_line() or self._touch_blocks(they)
        self._move_figure()

    def _touch_line(self):
        return sprite.is_collide_any_sprite(menu.line3, self.names)

    def _touch_blocks(self, they):
        for g in they:
            if sprite.is_collide_any_sprite(g['name'], self.names):
                return True
        return False

    def _move_figure(self):
        if self.check:
            return
        for i in self.names:
            sprite.move(i, 0, 5)

    def remove_figure_and_add_up(self):
        if not self.check:
            return
        for i in self.names:
            sprite.hide(i)
        self.names.clear()
        self.__init__(1)  # random value in one for 6
        self.check = not self.check

    def left(self, field):
        moving(self.calk_pos, self.names, 20, -30, 'right', field)

    def right(self, field):
        moving(self.calk_pos, self.names, 280, 30, "left", field)

    def down(self):
        for i in self.names:
            sprite.move(i, 0, 30)

    def Turn(self, fields):
        global danger
        # one
        # region
        if self.this_figure == 1 and self.turn == False:
            one = sprite.get_x(self.names[0])
            y = -30

            self.calk_pos.clear()
            for i in self.names:
                old_pos_x = sprite.get_x(i)
                old_pos_y = sprite.get_y(i)
                self.calk_pos.append(old_pos_x)
                self.calk_pos.append(old_pos_y)
            for i in self.names:
                sprite.move_to(i, one, sprite.get_y(i) + y)
                y -= 30
                for q in fields:
                    if sprite.is_collide_sprite(q['name'], i):
                        danger = True
            if danger == True:
                n = 0
                for i in self.names:
                    sprite.move_to(i, self.calk_pos[n], self.calk_pos[n + 1])
                    n += 2
            if danger == False:
                self.turn = not self.turn
            danger = False

        elif self.this_figure == 1 and self.turn == True:
            one = sprite.get_x(self.names[0])
            y = 30
            x = 0
            self.calk_pos.clear()
            for i in self.names:
                old_pos_x = sprite.get_x(i)
                old_pos_y = sprite.get_y(i)
                self.calk_pos.append(old_pos_x)
                self.calk_pos.append(old_pos_y)
            if sprite.get_x(self.names[0]) < 230:
                for i in self.names:
                    sprite.move_to(i, one + x, sprite.get_y(i) + y)
                    y += 30
                    x += 30
                    for q in fields:
                        if sprite.is_collide_sprite(q['name'], i):
                            danger = True
                if danger == True:
                    n = 0
                    for i in self.names:
                        sprite.move_to(i, self.calk_pos[n], self.calk_pos[n + 1])
                        n += 2
                if danger == False:
                    self.turn = not self.turn
                danger = False
        # endregion
        # two


def moving(calk_pos, names, count, move, left, field):
    global danger
    calk_pos.clear()
    moving = True

    for i in names:
        x = sprite.get_x(i)
        calk_pos.append(x)
    for i in calk_pos:
        if i >= count and left == "left":
            moving = False
        if i <= count and left == "right":
            moving = False
    calk_pos.clear()
    for i in names:
        old_x = sprite.get_x(i)
        old_y = sprite.get_y(i)
        calk_pos.append(old_x)
        calk_pos.append(old_y)
    for i in names:
        if moving:
            sprite.move(i, move, 0)
            for q in field:
                if sprite.is_collide_sprite(q['name'], i):
                    danger = True
                    break
    if danger == True:
        n = 0
        for i in names:
            sprite.move_to(i, calk_pos[n], calk_pos[n + 1])
            n += 2
    danger = False
