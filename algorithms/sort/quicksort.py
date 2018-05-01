
def get_pivot_index(array, first, last):
    """
    Function for getting pivot index.
    :param array: array with items <list>
    :param first: first index in array <int>
    :param last: last index in array <int>
    :return: median of first, mid, last values in array <int>
    """
    mid = (first + last) // 2
    pivot = last
    if array[first] < array[mid]:
        if array[mid] < array[last]:
            pivot = mid
    elif array[first] < array[last]:
        pivot = first
    return pivot


def partition(array, first, last):
    """
    Function for partitioning array.
    :param array: array with items <list>
    :param first: first index in array <int>
    :param last: last index in array <int>
    :return: pivot index <int>
    """
    pivot_index = get_pivot_index(array, first, last)
    pivot_value = array[pivot_index]
    border = first

    # swap pivot with first array item
    array[pivot_index], array[first] = array[first], array[pivot_index]

    for i in range(first, last + 1):
        if array[i] < pivot_value:
            border += 1
            array[i], array[border] = array[border], array[i]

    # swap border with pivot value
    # (as mentioned above, pivot is now at array[first])
    array[first], array[border] = array[border], array[first]

    # border now points to pivot index
    return border


def _quicksort(array, first, last):
    """
    Quicksort function
    :param array: array with items <list>
    :param first: first index in array <int>
    :param last: last index in array <int>
    """

    if first < last:
        pivot_index = partition(array, first, last)
        # left side
        _quicksort(array, first, pivot_index - 1)
        # right side
        _quicksort(array, pivot_index + 1, last)


def quicksort(array):
    """
    Wrapper for _quicksort function
    :param array: array with items <list>
    """
    first = 0
    last = len(array) - 1
    _quicksort(array, first, last)


if __name__ == '__main__':
    import time

    unsorted_array = [2, 3, 1, 7, 4, 4, 8]
    print(unsorted_array)
    print("Benchmark:")

    start_time = time.time()
    quicksort(unsorted_array)
    print(f'Quicksort: {time.time() - start_time}s')