class Error(Exception):
    def __init__(self, message=None):
        self.message = message


def factorial_with_exception(n, result):
    if n == 0:
        raise Error(message=result)
    factorial_with_exception((n-1), result*n)


def fibonacci_with_exception(n, wp, wpp):
    if n == 2:
        raise Error(message=wp+wpp)
    fibonacci_with_exception(n-1, wpp, wp+wpp)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibonacci(n-1) + fibonacci(n-2)


def fac(n):
    try:
        factorial_with_exception(n, 1)
    except Error as e:
        return e.message


def fib(n):
    try:
        fibonacci_with_exception(n, 0, 1)
    except Error as e:
        return e.message


print "Factorial WithoutExcept: ", factorial(19)
print "Factorial WithExcept:", fac(19)
print "\n"
print "Fibonacci WithoutExcept:", fibonacci(14)
print "Fibonacci WithExcept:", fib(14)