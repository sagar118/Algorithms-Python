"""
A pure python implementation of bubble sort algorithm
"""

def bubble_sort(arr: list) -> list:
    """
    Params:
        arr: A mutable collection

    Return:
        The same collection in sorted order

    Examples:
    >>> bubble_sort([5,2,1,7,6])
    [1, 2, 5, 6, 7]
    >>> bubble_sort([2, -5, 1, -2])
    [-5, -2, 1, 2]
    >>> bubble_sort([])
    []
    """

    length = len(arr)

    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j+1], arr[j] = arr[j], arr[j+1]

        if not swapped:
            break
    return arr

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    result = bubble_sort(collection)
    print(f"Sorted list: {result}")
