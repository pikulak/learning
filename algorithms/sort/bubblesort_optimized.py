
def bubble_sort_optimized(array):
    array_len = len(array)
    swapped = False

    for i in range(0, array_len - 1):
        n = 0
        while n < array_len - 1:
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
                swapped = True
            n += 1
            # omit the last one
            array_len -= 1

        # if nothing changes, break the loop
        if swapped:
            swapped = not swapped
        else:
            break

    return array


if __name__ == '__main__':
    import time
    from bubblesort import bubble_sort

    unsorted_array = [2, 3, 1, 7, 4, 4, 8]
    unsorted_array2 = unsorted_array[:]

    print("Benchmark:")

    start_time = time.time()
    bubble_sort(unsorted_array)
    print(f'Normal bubble sort: {time.time() - start_time}s')

    start_time_optimized = time.time()
    bubble_sort_optimized(unsorted_array2)
    print(f'Optimized bubble sort: {time.time() - start_time_optimized}s')
