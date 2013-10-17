#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from random import randint
import sys


class Player(object):
        def __init__(self):
            self.capacity = 0
            self.win = 0
            self.lose = 0
            self.roll = [0, 0]


class PlayRoll(object):

    def roll_of_the_dice(self):
        return randint(1, 6)

    def move(self, L):
        L[0].capacity = 0
        L[1].capacity = 0
        for j in range(2):
            L[j].roll[0] = self.roll_of_the_dice()
            L[j].roll[1] = self.roll_of_the_dice()
            L[j].capacity = L[j].capacity + (L[j].roll[0] + L[j].roll[1])
        if L[0].capacity > L[1].capacity:
            L[0].win += 1
            L[1].lose += 1
        else:
            L[0].lose += 1
            L[1].win += 1
        print '\nGracz 1 wyrzucił %d i %d\nBilans zwycięstwa/porażki %d/%d'\
              %(L[0].roll[0], L[0].roll[1], L[0].win, L[0].lose)
        print 'Gracz 2 wyrzucił %d i %d\nBilans zwycięstwa/porażki %d/%d\n'\
              %(L[1].roll[0], L[1].roll[1], L[1].win, L[1].lose)

    def play(self, n):
        player1 = Player()
        player2 = Player()
        L = [player1, player2]
        for i in xrange(n):
            self.move(L)
        while L[0].win == L[1].win:
            self.move(L)

        return L[0].win, L[1].win


if __name__ == "__main__":
    try:
        games = int(sys.argv[1])
    except Exception:
        games = int(raw_input('Podaj ilość tur: '))

    playgame = PlayRoll()
    p = playgame.play(games)
    print 'Wygrał: %s \n' %('Gracz 1' if p[0] > p[1] else 'Gracz 2')
