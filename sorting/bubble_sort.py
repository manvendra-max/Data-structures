def bubble_sort(inp):
    for i in range(len(inp)-1):
        for j in range(len(inp)-i-1):
            if inp[j] > inp[j+1]:
                inp[j], inp[j+1] = inp[j+1], inp[j]
    return inp

input_list = [1, 0, -98, 34,678,876876, 0,0,5,1,999999, 2]

if __name__ == '__main__':
    print(bubble_sort(input_list))
        

