
def swap_two(data_sequence:list, ind_b, ind_a):
    """This function swaps the values of 2 given indexes of the list"""
 
    first_val = data_sequence[ind_b]
    data_sequence.insert(ind_a + 1,first_val)
    data_sequence.pop(ind_b)



def bubble_sort(list_data):
    for i in range(len(list_data)-1, 0 , -1):
        for inner in range(i):
            if list_data[inner] > list_data[inner + 1]:
                swap_two(list_data, inner, inner + 1)
    return list_data

bub_result = bubble_sort([11,9,11,3, 1, 5, 8, 7])
print("Sorted Array is as Follows: ", bub_result)



def selection_sort(data:list):
    sorted_arrray = []
    lowest = data[0]

    while data:
        lowest = data[0]
        for i in data:
            if i < lowest:
                lowest = i
        data.remove(lowest)
        sorted_arrray.append(lowest)

    return sorted_arrray

print(f"The sorted array is as follows: {selection_sort([4,2,7,1,6,8])}")



