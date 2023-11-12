import numpy as np
import time


def merge_sort(array):

    if len(array) <= 1:
        return array

    left_array = array[:len(array)//2]
    right_array = array[len(array)//2:]

    merge_sort(left_array)
    merge_sort(right_array)

    i = j = k = 0
    while i < len(left_array) and j < len(right_array):

        if left_array[i] < right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1

    while i < len(left_array):
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < len(right_array):
        array[k] = right_array[j]
        j += 1
        k += 1

    return array

def binary_sort(array):
    if len(array) <= 1:
        return array

    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def time_it(begin, end):
    return end - begin


if __name__ == "__main__":
    unsorted_array = [i for i in np.random.randint(0, 1000, 10000)]
    print('Before sorting -', unsorted_array)

    start = time.time()
    sorted_array = merge_sort(unsorted_array)
    stop = time.time()
    print('Time taken for merge sorting execution', time_it(start, stop), ' Seconds')

    # start = time.time()
    # sorted_array = binary_sort(unsorted_array)
    # stop = time.time()
    # print('Time taken for binary sorting execution', time_it(start, stop), ' Seconds')
    print('After sorting -', sorted_array)
