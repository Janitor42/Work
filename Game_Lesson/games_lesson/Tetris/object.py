import random
import time
import wrap
from wrap import sprite, sprite_text, world
import menu
import field

check = False


class Figure():
    def __init__(self, rd):
        if rd == 1:
            x = 320
            y = 0
            self.names = []
            self.rd = rd
            self.turn = False
            for i in range(4):
                self.names.append(sprite.add('pacman', x, y, 'dot'))
                sprite.set_size(self.names[-1], 28, 28)
                x += 30

        if rd == 2:
            x = 320
            y = 0
            self.names = []
            self.rd = rd
            for i in range(4):
                self.names.append(sprite.add('pacman', x, y, 'dot'))
                sprite.set_size(self.names[-1], 28, 28)
                x += 30
                if i == 1:
                    y = -30
                    x = 320

    # wrong it's here
    def work_platform(self, they):
        global check
        for i in self.names:
            if sprite.is_collide_sprite(i, menu.line3):
                for g in self.names:
                    sprite.move_to(g, sprite.get_x(g), sprite.get_y(g) + 10)
                check = True
                break
            for g in they:
                if sprite.is_collide_sprite(i, g['name']):
                    check = True
                    break
        if not check:
            for i in self.names:
                sprite.move(i, 0, 5)

    def remove_names(self):
        global check
        if check:
            for i in self.names:
                sprite.hide(i)
            self.names.clear()
            self.__init__(1)  # random value in one for 6
            check = not check

    def left(self):
        for i in self.names:
            sprite.move(i, -30, 0)

    def right(self):
        for i in self.names:
            sprite.move(i, 30, 0)

    def down(self):
        for i in self.names:
            sprite.move(i, 0, 30)

    def Turn(self):
        # one
        if self.rd == 1 and self.turn == False:
            one = sprite.get_x(self.names[0])
            y = -30
            for i in self.names:
                sprite.move_to(i, one, sprite.get_y(i) + y)
                y -= 30
            self.turn = not self.turn
        elif self.rd == 1 and self.turn == True:
            one = sprite.get_x(self.names[0])
            y = 30
            x = 0
            for i in self.names:
                sprite.move_to(i, one + x, sprite.get_y(i) + y)
                y += 30
                x += 30
            self.turn = not self.turn
