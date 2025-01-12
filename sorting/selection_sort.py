def selection_sort(input_list : list) -> list:
    for i in range(len(input_list)-1):
        min_index = i
        for j in range(i+1, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]

input_list = [1, 0, -98, 34,678,876876, 0,0,5,1,999999]

if __name__ == '__main__':
    selection_sort(input_list)
    print(input_list)

