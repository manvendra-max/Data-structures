def bubble_rec(input_list: list, n) -> None:
    if n == 1:
        return
    for i in range(0, n-1):
        if input_list[i] > input_list[i+1]:
            input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
    bubble_rec(input_list, n-1)
    return input_list

if __name__ == "__main__":
    il = [1,3,2,5,4,3,7,8,1]
    print(bubble_rec(il, len(il)))
    
