"""
A pure python implementation of randomized quick sort. Partition scheme in quick sort can be done in 
two ways: Hoare's partition scheme and Lomuto partition scheme.
"""

import random

def random_partition(arr: list, low: int, high: int, scheme="lomuto") -> int:
    """
    Generating a random number between the starting index of the array and the ending index 
    of the array. Swaps the value at index low with randomly generated index for hoare scheme. 
    For lomuto's scheme swaps the value at index high with the randomly generated index value.

    Params:
        arr: A mutable collection that needs to be sorted
        low: left endpoint of sorting
        high: right endpoint of sorting
        scheme: partitioning scheme. Default value is lomuto

    Returns:
        index: Partitioning index
    """
    pivot_index = random.randrange(low, high)
    if scheme == "hoare":
        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]
        return hoare_partition(arr, low, high)
    else:
        arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
        return lomuto_partition(arr, low, high)

def lomuto_partition(arr: list, low: int, high: int) -> int:
    """
    This function takes last element as pivot, places the pivot element at its correct position in 
    sorted array, and places all smaller (smaller than pivot) to left of pivot and all greater 
    elements to right of pivot.

    Params:
        arr: A mutable collection that needs to be sorted
        low: left endpoint of sorting
        high: right endpoint of sorting
    
    Retuns:
        i: Index of the pivot at the correct position
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def hoare_partition(arr: list, low: int, high: int) -> int:
    """
    This function takes first element as pivot, and places all the elements smaller than the pivot 
    on the left side and all the elements greater than the pivot on the right side. It returns the 
    index of the last element on the smaller side.

    Params:
        arr: A mutable collection that needs to be sorted
        low: left endpoint of sorting
        high: right endpoint of sorting
    
    Retuns:
        i: Index of the last element on the smaller side
    """
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i < j:       
            arr[i], arr[j] = arr[j], arr[i]
        else:
            return j

def quick_sort(arr: list, low: int, high: int, scheme="lomuto") -> None:
    """
    The main function that implements QuickSort.

    Params:
        arr: A mutable collection that needs to be sorted
        low: left endpoint of sorting
        high: right endpoint of sorting
        scheme: partitioning scheme. Default value is lomuto

    Returns:
        None
    
     Examples:
    >>> nums1 = [0, 5, 3, 1, 2]
    >>> quick_sort(nums1, 0, 4)
    >>> nums1
    [0, 1, 2, 3, 5]
    >>> nums2 = []
    >>> quick_sort(nums2, 0, 0)
    >>> nums2
    []
    >>> nums3 = [-2, 5, 0, -4]
    >>> quick_sort(nums3, 0, 3, scheme="hoare")
    >>> nums3
    [-4, -2, 0, 5]
    """
    if low < high:
        if scheme == 'hoare':
            pi = random_partition(arr, low, high, "hoare") # pi is partitioning index
            quick_sort(arr, low, pi, "hoare")
            quick_sort(arr, pi + 1, high, "hoare")
        else:
            pi = random_partition(arr, low, high) # pi is partitioning index
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(element.strip()) for element in user_input.split(',')]

    n = len(collection)
    quick_sort(collection, 0, n - 1)
    # quick_sort(collection, 0, n - 1, scheme="hoare")
    print(f"Sorted list: {collection}")