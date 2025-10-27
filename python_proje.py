#1

input_list = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(input_list):
    flattened_list = []
    for i in input_list:
        if isinstance(i,list):
            flattened_list.extend(flatten(i))
        else:
            flattened_list.append(i)
    return flattened_list
result = flatten(input_list)
print(result)


#2

input_list2 = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(input_list2):
    reverse_list = input_list2[::-1]
    for i in range(len(reverse_list)):
        j = reverse_list[i]
        if isinstance(j, list):
            reverse_list[i] = reverse(j)
    return reverse_list
result2 = reverse(input_list2)
print(result2)