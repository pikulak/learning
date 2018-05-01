
def bubblesort(array):
    array_len = len(array)
    for i in range(0, array_len - 1):
        for n in range(0, array_len - 1):
            if array[n] > array[n+1]:
                array[n], array[n+1] = array[n+1], array[n]
    return array


if __name__ == '__main__':
    import time

    unsorted_array = [2, 3, 1, 7, 4, 4, 8]
    print(unsorted_array)
    print("Benchmark:")

    start_time = time.time()
    bubblesort(unsorted_array)
    print(f'Bubblesort: {time.time() - start_time}s')