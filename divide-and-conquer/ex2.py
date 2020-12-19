# Algorithm for Counting Inversions based on merge sort algorithm
from typing import List


def getInput(file: str) -> list:
    dt = []
    with open(file, "r") as file:
        for line in file:
            dt.extend(line.split())
    return list(map(int, dt))


def merge_sort_inversion(a: List[int]) -> (List[int], int):
    if len(a) < 2:
        return a, 0
    mid = len(a)//2
    left, inver_l = merge_sort_inversion(a[:mid])
    right, inver_r = merge_sort_inversion(a[mid:])
    a_sorted = []
    i = j = 0
    inver = 0 + inver_l + inver_r
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_sorted.append(left[i])
            i += 1
        else:
            a_sorted.append(right[j])
            j += 1
            inver += len(left)-i
    if (i < len(left)):
        a_sorted.extend(left[i:])
    else:
        a_sorted.extend(right[j:])
    return a_sorted, inver


if __name__ == "__main__":
    # test cases
    assert merge_sort_inversion([1, 3, 5, 2, 4, 6]) == ([1, 2, 3, 4, 5, 6], 3)
    assert merge_sort_inversion([1, 2, 4, 3, 5, 6]) == ([1, 2, 3, 4, 5, 6], 1)
    assert merge_sort_inversion([1, 2, 4, 3, 5, 6, 8, 7, 9]) == ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
    arr = getInput('IntegerArray.txt')
    arr_sorted, inversions = merge_sort_inversion(arr)
    print('The number of the inversions in the array is:', inversions)
