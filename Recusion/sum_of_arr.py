def sm(arr):
    n = len(arr)
    if n == 0:
        return
    if n == 1:
        return arr[0]
    s1 = sm(arr[1:])
    # s2 = sm(n-2)
    return s1+arr[0]

print(sm([5,2,3,5]))