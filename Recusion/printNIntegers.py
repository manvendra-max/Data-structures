n = int(input())

def rec(n):
    if n ==0 :
        print(0)
    else:
        rec(n-1)
        print(n)

rec(n)