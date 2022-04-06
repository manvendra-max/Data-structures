#the function returns n to the power x

num = int(input("enter the number"))
pow = int(input("raise to the power?"))
def power(n,x):
    if x == 0:
        return 1
    s = n * power(n,x-1)
    return s
print(power(num, pow))
