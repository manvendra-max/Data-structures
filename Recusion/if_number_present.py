def isThere(arr, num):
    n = len(arr)
    if n == 0:
        return False
    if arr[0]== num:
        return True
    shortArray = isThere(arr[1:], num)
    return shortArray

print(isThere([10,20,23,25,66,77,56], 66))

print(isThere([10,20,23,25,66,77,56], 90))
