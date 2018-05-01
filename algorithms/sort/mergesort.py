import sys


def merge(array, first, middle, last):
    """
    Function for merging array.
    :param array: array with items <list>
    :param first: first index in array <int>
    :param middle: middle index in array <int>
    :param last: last index in array <int>
    """
    left = array[first:middle]
    right = array[middle:last + 1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)

    i = j = 0
    for k in range(first, last + 1):
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1


def _mergesort(array, first, last):
    """
    Merge sort function.
    :param array: array with items <list>
    :param first: first index in array <int>
    :param last: last index in array <int>
    """

    if first < last:
        middle = (first + last) // 2

        # left side
        _mergesort(array, first, middle)
        # right side
        _mergesort(array, middle + 1, last)

        # combine two lists together
        merge(array, first, middle + 1, last)


def mergesort(array):
    """
    Wrapper for _merge function
    :param array: array with items <list>
    """
    first = 0
    last = len(array) - 1
    _mergesort(array, first, last)


if __name__ == '__main__':
    import time

    unsorted_array = [2, 3, 1, 7, 4, 4, 8]
    print(unsorted_array)
    print("Benchmark:")

    start_time = time.time()
    mergesort(unsorted_array)
    print(f'Mergesort: {time.time() - start_time}s')