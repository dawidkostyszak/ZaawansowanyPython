"""
Author: Dawid Kostyszak
Lista 2 zadanie 3
Deadline: 29.10.2013
"""
import timeit
from lista4zad1_cz2 import (
    pierwsze_funkcyjna,
    pierwsze_skladana,
    pierwsze_iteracyjna,
    pierwsze_iteracyjna2,
)
print "n | funkcyjna | skladana | iteracyjna | iteracyjna2"
L = [10, 100, 1000]

for n in L:
    skladana = timeit.Timer(
        "lista4zad1_cz2.pierwsze_skladana(%s)" % n, "import lista4zad1_cz2"
    )
    funkcyjna = timeit.Timer(
        "lista4zad1_cz2.pierwsze_funkcyjna(%s)" % n, "import lista4zad1_cz2"
    )
    iteracyjna = timeit.Timer(
        "lista4zad1_cz2.pierwsze_iteracyjna(%s)" % n, "import lista4zad1_cz2"
    )
    iteracyjna2 = timeit.Timer(
        "lista4zad1_cz2.pierwsze_iteracyjna2(%s)" % n, "import lista4zad1_cz2"
    )

    t1 = skladana.timeit(number=10000)
    t2 = funkcyjna.timeit(number=10000)
    t3 = iteracyjna.timeit(number=10000)
    t4 = iteracyjna2.timeit(number=10000)

    pierwsze_skladana(n)
    pierwsze_funkcyjna(n)

    pierwsze_iteracyjna(n)
    pierwsze_iteracyjna2(n)


    print "%d | %f | %f | %f | %f" %(n, t1, t2, t3, t4)