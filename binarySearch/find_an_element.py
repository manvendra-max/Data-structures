def binary_search(arr, k):
    n = len(arr)
    low = 0
    high = n-1
    mid = (low+high)//2

    while (low <= high):
        if arr[mid] == k:
            return mid
        
        elif (arr[mid] < k):
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + high)//2
    return "Elemtn not found"

arr = [0,1,3,5,6,7,8]
print(binary_search(arr, 82))

