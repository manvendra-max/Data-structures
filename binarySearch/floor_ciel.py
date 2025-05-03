def floor_ciel(arr: list, x: int) -> list: 
    
    n = len(arr)
    low = 0
    high = n-1
    ciel_val = float("inf")
    floor_val = float("-inf")

    while (low <= high):
        mid = (low+high)//2
        if arr[mid] == x:
            ciel_val , floor_val = arr[mid], arr[mid]
            return [floor_val, ciel_val]
        elif arr[mid] > x:
            ciel_val = min(ciel_val, arr[mid])
            high = mid - 1
        else:
            floor_val = max(floor_val, arr[mid])
            low = mid + 1
    return [floor_val, ciel_val]

arr = [3, 4, 4, 7, 8, 10]
print(floor_ciel(arr, 8))


