def insertion_sort(arr: list) -> list:
    for i in range(len(arr)-1):
        j = i+1
        while (j>0 and (arr[j-1] > arr[j])):
            print("inside")
            arr[j], arr[j-1] = arr[j -1], arr[j]
            j = j-1
    return arr 
        
input_list = [1, -2,2,-23,4,5,0]

"""
Time complexity
best = n
avg = n^2
worst = n^2
"""


if __name__ == '__main__':
    print(insertion_sort(input_list))
    
      