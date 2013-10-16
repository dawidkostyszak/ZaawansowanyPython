import timeit


fac_t = timeit.Timer("a.factorial(19)", "import a")
facexc_t = timeit.Timer("a.fac(19)", "import a")
fib_t = timeit.Timer("a.fibonacci(8)", "import a")
fibexc_t = timeit.Timer("a.fib(8)", "import a")

t1 = fac_t.timeit()
t2 = facexc_t.timeit()
t3 = fib_t.timeit()
t4 = fibexc_t.timeit()

print "Time normal factorial:", t1
print "Time other factorial:", t2
print "\n"
print "Time normal fibonacci:", t3
print "Time other fibonacci:", t4