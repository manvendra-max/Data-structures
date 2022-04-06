def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    s1 = fib(n-1)
    s2 = fib(n-2)
    return s1 + s2
print(fib(6)) 