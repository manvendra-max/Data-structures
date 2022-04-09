from sympy import false, true


def isSorted(arr, n):
    if n == 0 or n == 1:
        return true
    if arr[0]>arr[1]:
        return false
    
    return isSorted(arr[1:],n-1)

print(isSorted([3,4,5,10,20],5))

