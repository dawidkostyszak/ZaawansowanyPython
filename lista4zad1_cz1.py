"""
Author: Dawid Kostyszak
Lista 2 zadanie 3
Deadline: 29.10.2013
"""
import timeit
print "n    | funkcyjna | skladana | iteracyjna | iteracyjna2"
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

    t1 = skladana.timeit(number=100)
    t2 = funkcyjna.timeit(number=100)
    t3 = iteracyjna.timeit(number=100)
    t4 = iteracyjna2.timeit(number=100)


    print "%d" %n + (4-len(str(n)))*' '+' | %f  | %f | %f   | %f' %(t1, t2, t3, t4)