"""
Author: Dawid Kostyszak
Lista 2 zadanie 3
Deadline: 29.10.2013
"""
import timeit
import lista3_cz2

n = 20

skladana = timeit.Timer(
    "lista3_cz2.pierwsze_skladana(%s)" % n, "import lista3_cz2"
)
funkcyjna = timeit.Timer(
    "lista3_cz2.pierwsze_funkcyjna(%s)" % n, "import lista3_cz2"
)

t1 = skladana.timeit(number=10000)
t2 = funkcyjna.timeit(number=10000)

print lista3_cz2.pierwsze_skladana(n)
print t1
print "\n"
print lista3_cz2.pierwsze_funkcyjna(n)
print t2
