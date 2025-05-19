#the function returns n to the power x

num = int(input("enter the number"))
pow = int(input("raise to the power?"))
def power(n,x):
    if x == 0:
        return 1
    s = n * power(n,x-1)
    return s
print(power(num, pow))

# optimised version
# exponentiation by squaring
def pow(x, n):
    ans = 1
    nn = n
    while nn > 0:
        if nn%2 == 0:
            # If nn is even, the algorithm can simplify the computation by 
            # squaring the base and halving the exponent.
            x = x * x
            nn = nn//2
        else:
            ans = ans * x
            nn -= 1
    return ans

print(pow(2,3))
