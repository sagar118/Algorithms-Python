"""
A pure python implementation of insertion sort incorporated in merge sort. Since insertion sort
is faster for small amounts of inputs.
"""

def insertion_sort(arr: list, low: int, high: int) -> None:
    """
    Function perform in-place sort operation

    Params:
        arr: A mutable collection
        low: Lower Bound
        high: Upper bound

    Returns:
        None
    """

    for index in range(low+1, high+1):
        item = arr[index]
        while (index > low) and (arr[index - 1] > item):
            arr[index] = arr[index - 1]
            index -= 1
        arr[index] = item

def merge_insertion_sort(arr: list, low: int, high: int) -> list:
    """
    Function perform in-place sort operation

    Params:
        arr: A mutable collection
        low: Lower Bound
        high: Upper bound

    Returns:
        The same collection in sorted order
    """

    if high - low <= THRESHOLD:
        insertion_sort(arr, low, high)
    else:
        mid = (low + high) // 2
        merge_insertion_sort(arr, low, mid)
        merge_insertion_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr: list, low: int, mid: int, high: int) -> None:
    """
    Function performs the combine operation and sorts the two sub-problems.

    Params:
        arr: A mutable collection
        low: Lower Bound
        mid: Middle index
        high: Upper bound

    Returns:
        None
    """

    left, right = list(), list()
    i, j, k = (0, 0, low)
    left, right = (arr[low: mid+1], arr[mid+1: high+1])
    n1 = mid - low + 1
    n2 = high - mid

    while (i < n1) and (j < n2):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

if __name__ == '__main__':
    from doctest import testmod

    THRESHOLD = 20

    # testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    merge_insertion_sort(collection, 0, len(collection)-1)
    # insertion_sort(collection)
    print(f"Sorted list: {collection}")
