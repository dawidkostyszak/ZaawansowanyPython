"""
Author: Dawid Kostyszak
Lista 2 zadanie 3
Deadline: 22.10.2013
"""
import timeit
import lista2_cz2 as zad


fac_n = 19
fib_n = 14

fac_t = timeit.Timer("lista2_cz2.factorial(%s)" % fac_n, "import lista2_cz2")
facexc_t = timeit.Timer("lista2_cz2.fac(%s)" % fac_n, "import lista2_cz2")
fib_t = timeit.Timer("lista2_cz2.fibonacci(%s)" % fib_n, "import lista2_cz2")
fibexc_t = timeit.Timer("lista2_cz2.fib(%s)" % fib_n, "import lista2_cz2")

t1 = fac_t.timeit()
t2 = facexc_t.timeit()
t3 = fib_t.timeit()
t4 = fibexc_t.timeit()

print "Factorial WithoutExcept:", zad.factorial(fac_n)
print "Factorial WithExcept:", zad.fac(fac_n)
print "Time normal factorial:", t1
print "Time other factorial:", t2
print "\n"
print "Fibonacci WithoutExcept:", zad.fibonacci(fib_n)
print "Fibonacci WithExcept:", zad.fib(fib_n)
print "Time normal fibonacci:", t3
print "Time other fibonacci:", t4
