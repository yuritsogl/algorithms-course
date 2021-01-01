'''
The program Computes the total number of comparisons used to sort a given input file by QuickSort using different pivots rules:
1. The first element of the array defined as the pivot.
2. The last element of the array  defined as the pivot.
3. The pivot is defined by the "median-of-three" rule.
'''

from typing import List

count = 0


def getInput(file: str) -> list:
    dt = []
    with open(file, "r") as file:
        for line in file:
            dt.extend(line.split())
    return list(map(int, dt))


def quicksort(a: List[int], flag) -> (list, int):
    n = len(a)
    k = calc_pivot(a, flag)
    if (n < 2):
        return a
    a[k], a[0] = a[0], a[k]
    k = 0
    a, piv_pos = partition(a, k, n)
    small = quicksort(a[:piv_pos], flag)
    big = quicksort(a[piv_pos+1:], flag)
    small.append(a[piv_pos])
    a_sorted = []
    a_sorted.extend(small+big)
    return a_sorted


def partition(a: List[int], l: int, r: int) -> (list, int):
    global count
    count += r - 1
    p = a[l]
    i, j = l + 1, l + 1
    for j in range(r):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[l], a[i-1] = a[i-1], a[l]
    return a, i-1


def calc_pivot(a: List[int], flag) -> int:
    global count
    n = len(a) - 1
    if flag == 1:
        return 0
    elif flag == 2:
        return -1
    elif flag == 3:
        if (n < 2):
            return 0
        pivot_options = {
            a[0]: 0,
            a[n//2]: n//2,
            a[-1]: n
            }
        pivot = list(pivot_options.keys())
        count_temp = count
        pivot = quicksort(pivot, 1)  # Use quiksort to sort the list
        count = count_temp  # Offset the comparisons made
        return pivot_options[pivot[1]]
    else:
        print("Oops!  That was not a valid flag. Please Try again...")
        raise ValueError


if __name__ == "__main__":
    # test cases
    assert quicksort([1, 3, 2], 1) == [1, 2, 3]
    assert quicksort([3, 1, 2], 2) == [1, 2, 3]
    assert quicksort([1, 2, 3], 3) == [1, 2, 3]
    assert quicksort([2, 3, 1], 1) == [1, 2, 3]
    assert quicksort([2, 1, 3], 2) == [1, 2, 3]
    assert quicksort([4, 1, 6, 3, 2, 7, 5], 3) == [1, 2, 3, 4, 5, 6, 7]
    assert quicksort([5, 2, 3, 7, 1, 6, 4], 1) == [1, 2, 3, 4, 5, 6, 7]
    assert quicksort([4, 1, 6, 6, 3, 2, 7, 5], 2) == [1, 2, 3, 4, 5, 6, 6, 7]
    assert quicksort([4, 1, 6, 6, 3, 2, 7, 5, 5], 3) == [1, 2, 3, 4, 5, 5, 6, 6, 7]
    count = 0

    arr = getInput('QuickSort.txt')
    arr_sorted_1, compare_num_1 = quicksort(arr.copy(), 1), count
    count = 0
    arr_sorted_2, compare_num_2 = quicksort(arr.copy(), 2), count
    count = 0
    arr_sorted_3, compare_num_3 = quicksort(arr.copy(), 3), count
    print('The number of comparisons in the first exercise is:', compare_num_1)
    print('The number of comparisons in the second exercise is:', compare_num_2)
    print('The number of comparisons in the third exercise is:', compare_num_3)
