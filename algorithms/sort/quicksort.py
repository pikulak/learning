
def get_pivot_index(array, begin, end):
    """
    Function for getting pivot index.
    :param array: array with items <list>
    :param begin: start index in array <int>
    :param end: last index in array <int>
    :return: median of begin, mid, end values in array <int>
    """
    mid = (begin + end) // 2
    pivot = end
    if array[begin] < array[mid]:
        if array[mid] < array[end]:
            pivot = mid
    elif array[begin] < array[end]:
        pivot = begin
    return pivot


def partition(array, begin, end):
    """
    Function for partitioning array.
    :param array: array with items <list>
    :param begin: start index in array <int>
    :param end: last index in array <int>
    :return: pivot index <int>
    """
    pivot_index = get_pivot_index(array, begin, end)
    pivot_value = array[pivot_index]
    border = begin

    # swap pivot with first array item
    array[pivot_index], array[begin] = array[begin], array[pivot_index]

    for i in range(begin, end + 1):
        if array[i] < pivot_value:
            border += 1
            array[i], array[border] = array[border], array[i]

    # swap border with pivot value
    # (as mentioned above, pivot is now at array[begin])
    array[begin], array[border] = array[border], array[begin]

    # border now points to pivot index
    return border


def _quicksort(array, begin, end):
    """
    Quicksort function
    :param array: array with items <list>
    :param begin: start index in array <int>
    :param end: last index in array <int>
    """

    if begin < end:
        pivot_index = partition(array, begin, end)
        # left side
        _quicksort(array, begin, pivot_index - 1)
        # right side
        _quicksort(array, pivot_index + 1, end)


def quicksort(array):
    """
    Wrapper for _quicksort function
    :param array: array with items <list>
    """
    begin = 0
    end = len(array) - 1
    _quicksort(array, begin, end)


if __name__ == '__main__':
    import time

    unsorted_array = [2, 3, 1, 7, 4, 4, 8]
    print(unsorted_array)
    print("Benchmark:")

    start_time = time.time()
    quicksort(unsorted_array)
    print(f'Quicksort: {time.time() - start_time}s')