
def bubble_sort(array):
    array_len = len(array)
    for i in range(0, array_len - 1):
        for n in range(0, array_len - 1):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array


unsorted_array = [2, 3, 1, 7, 4, 4, 8]
print(bubble_sort(unsorted_array))