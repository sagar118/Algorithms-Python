"""
A pure python implementation of merge sort
"""

def merge_sort(arr: list, low: int, high: int) -> list:
    """
    Function that divides and latter call the merge function to perform combine operation.

    Params:
        arr: A mutable collection
        low: Lower bound
        high: Upper bound
    
    Return:
        The same collection in sorted order

    Examples:
    >>> merge_sort([5,1,7,2,6], 0, 4)
    [1, 2, 5, 6, 7]
    >>> merge_sort([12,2,-45,-2], 0, 3)
    [-45, -2, 2, 12]
    >>> merge_sort([], 0, -1)
    []
    """
    if (low < high):
        mid = (low + high)//2
        # print(mid)
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr

def merge(arr: list, low: int, mid: int, high: int) -> None:
    """
    Function that combines the sub-problems which results the combined solution is in sorted order.
    Params:
        arr: A mutable collection
        low: Lower bound
        mid: Middle index
        high: Upper bound
    
    Returns;
        None
    """

    left, right = list(), list()
    i, j, k = (0, 0, low)
    n1 = mid - low + 1
    n2 = high - mid

    left = arr[low:mid+1]
    right = arr[mid+1:high+1]

    while (i < n1) and (j < n2):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while (i < n1):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while (j < n2):
        arr[k] = right[j]
        k += 1
        j += 1

if __name__ == '__main__':
    from doctest import testmod

    testmod()    
    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    merge_sort(collection, 0, len(collection)-1)
    print(f"Sorted list: {collection}")
