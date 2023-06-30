#!/usr/bin/python3
"""6-peak module:
    defines find_peak funciton"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    arr = list_of_integers
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if (
                (mid == 0 or arr[mid] >= arr[mid - 1])
                and (mid == len(arr) - 1 or arr[mid] >= arr[mid + 1])
                ):
            return arr[mid]
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            high = mid - 1
        else:
            low = mid + 1
    return None
