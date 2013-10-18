"""
Author: Dawid Kostyszak
Lista 3 zadanie 1
Deadline: 29.10.2013
"""


def pierwsze_skladana(n):
    return [i for i in xrange(2, n+1)
            if len([j for j in xrange(1, n+1)if i % j == 0]) == 2]


def pierwsze_funkcyjna(n):
    L = range(2, n+1)

    def cos(x):
        D = range(1, x+1)

        def mod(y):
            return x % y == 0

        if map(mod, D).count(True) == 2:
            return True
        else:
            return False

    return filter(cos, L)
