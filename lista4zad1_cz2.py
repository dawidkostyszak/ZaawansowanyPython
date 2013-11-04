"""
Author: Dawid Kostyszak
Lista 4 zadanie 1
Deadline: 05.11.2013
"""


def pierwsze_skladana(n):
    return [i for i in xrange(2, n + 1)
            if len([j for j in xrange(1, n + 1)if i % j == 0]) == 2]


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


def pierwsze_iteracyjna(n):
    L = []
    for i in range(2, n):
        pierwsza = True
        for j in range(2, i):
            if i % j == 0:
                pierwsza = False
                break
        if pierwsza:
            L.append(i)
    return L


def pierwsze_iteracyjna2(n):
    D = []
    L = []
    for i in range(2, n):
        pierwsza = True
        for j in D:
            if i % j == 0:
                pierwsza = False
                break
        if pierwsza:
            D.append(i)
            L.append(i)
    return L