def Permutations():
    numb_of_items = int(input())
    order = input().split()
    numbers = input().split()
    result = []

    for item in range(numb_of_items):
       
       find_index = order.index(str(item + 1))
       result.append(numbers[find_index])

    print(result)


Permutations()