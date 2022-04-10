from more_itertools import first


def firstIndex(arr, x):
    n = len(arr)
    if n == 0 :
        print("n==0 pe aya")
        return -1
    if arr[0] == x:
        print("arr of 0 pe ruka")
        return 0   
    shortArray = firstIndex(arr[1:], x)
    if shortArray == -1:
        return -1
    return (shortArray + 1)

print(firstIndex([1,2,7,7,8,6,5], 5))