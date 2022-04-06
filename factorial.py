num = int(input("enter a number whose factorial is to be calculated:"))
def fact(n):
    if n == 0:
        return 1
    sm = 1
    sm = n*fact(n-1)
    return sm
print(fact(num))

