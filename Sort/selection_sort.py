"""
A pure python implementation of Selection Sort
"""

def selection_sort(arr: list) -> list:
    """
    Function to sort the collection.

    Params:
        arr: mututable collection

    Return:
        The same collection in sorted order

    Examples:
    >>> selection_sort([5, 1, 6, 2, 7])
    [1, 2, 5, 6, 7]
    >>> selection_sort([])
    []
    >>> selection_sort([-45, -5, -10])
    [-45, -10, -5]
    """

    length = len(arr)
    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = (arr[min_index], arr[i])
    return arr

if __name__ == '__main__':

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    result = selection_sort(collection)
    print(f"Sorted list: {result}")
