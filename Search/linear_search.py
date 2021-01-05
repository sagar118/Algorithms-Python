"""
A pure python implementation of linear search
"""

def linear_search(arr: list, target: int) -> int:
    """
    Iterative method of implementing linear search

    :params arr: a collection with comparable items
    :params target: item value to search
    :return: index of found item or -1 if item not found

    Examples:
    >>> linear_search([1,2,3], 3)
    2
    >>> linear_search([25, 4, 51, 2], 4)
    1
    >>> linear_search([4, 6, 1, 10], 0)
    -1
    >>> linear_search([], 2)
    -1
    """

    for index, item in enumerate(arr):
        if item == target:
            return index
    return -1

def rec_linear_search(arr: list, low: int, high: int, target: int) -> int:
    """
    Recursive implementation of linear search

    Params:
        arr: A collection with comparable items
        low: Lower bound of the list
        high: Upper bound of the list
        target: Item to be searched in the list

    Return:
        Index of the target if found. Otherwise, -1

    Examples:
    >>> rec_linear_search([1,2,3], 0, 2, 3)
    2
    >>> rec_linear_search([25, 4, 51, 2], 0, 3, 4)
    1
    >>> rec_linear_search([4, 6, 1, 10], 0, 3,0)
    -1
    """

    if not ((0 <= low < len(arr)) and (0 <= high < len(arr))):
        raise Exception("Invalid upper or lower bounds")

    if high < low:
        return -1

    if arr[low] == target:
        return low
    if arr[high] == target:
        return high

    return rec_linear_search(arr, low + 1, high - 1, target)

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input('Enter numbers separated by comma:\n')
    key = int(input('Enter a single number to be searched in the list:\n').strip())

    if len(user_input) == 0:
        RESULT = -1
    else:
        sequence = [int(item.strip()) for item in user_input.split(",")]

        RESULT = linear_search(sequence, key) # Call Iterative linear search

        # Call Recursive linear search
        # RESULT = rec_linear_search(sequence, 0, len(sequence)-1, key)

    if RESULT != -1:
        print(f"Item found at location {RESULT}")
    else:
        print(f"{key} was not found in the list")
