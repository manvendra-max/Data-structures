def lower_bound(arr, target):
    """ 
    return the lowest index of the element which is grater than or equals to target
    return i such that arr[i] >= target 
    """

    n = len(arr)
    low = 0
    high = n-1
    result = float("inf")

    while (low <= high):
        mid = (low+high)//2

        if arr[mid] >= target:
            result = min(mid, result)
        
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


arr = [1,2,2,9,10,90]


print(lower_bound(arr,7))

