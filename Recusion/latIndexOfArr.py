
def lastIndex(arr, x):
    n = len(arr)
    if n == 0:
        return -1
    if arr[n-1] == x:
        return (n-1)
    ans = lastIndex(arr[:n-1], x)
    return ans
print(lastIndex([20,30,5,6,6,7,20], 6))
    