import numpy as np
import time
from Sorting_algorithms import merge_sort


def linear_search(array, value):
    for index, item in enumerate(array):
        if value == item:
            return index, array[index]
    return None, value


def binary_search(array, value):

    left_index = 0
    right_index = len(array) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if array[mid_index] == value:
            return mid_index, array[mid_index]

        elif array[mid_index] < value:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return None, value


def time_it(begin, end):
    return end - begin


if __name__ == "__main__":
    array = [i for i in np.random.randint(0, 10000, 10000)]
    sorted_array = merge_sort(array)
    value = np.random.choice(array)
    print(sorted_array)

    start = time.time()
    print(linear_search(array, value))
    stop = time.time()
    print('Time taken for linear search execution', time_it(start, stop), ' Seconds')

    start = time.time()
    print(binary_search(sorted_array, value))
    stop = time.time()
    print('Time taken for binary search execution', time_it(start, stop), ' Seconds')