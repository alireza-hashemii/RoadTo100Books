
def swap_two(data_sequence:list, ind_b, ind_a) -> list:
    """This function swaps the values of 2 given indexes of the list"""
    data_sequence_copy = data_sequence.copy()
    first_val = data_sequence_copy[ind_b]
    data_sequence_copy.insert(ind_a + 1,first_val)
    data_sequence_copy.pop(ind_b)
    return data_sequence_copy


def bubble_sort(list_data):
    for i in range(len(list_data)-1, 0 , -1):
        for inner in range(i):
            if list_data[inner] > list_data[inner + 1]:
                list_data = swap_two(list_data, inner, inner + 1)
    return list_data

bub_result = bubble_sort([11,9,11,3, 1, 5, 8, 7])
print("Sorted Array is as Follows: ", bub_result)