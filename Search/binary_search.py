"""
A pure python implementation of binary search
"""

def binary_search(arr: list, low: int, high: int, target: int) -> int:
    """
    Params:
        arr: A mutable collection in sorted order (ascending)
        low: Lower bound
        high: Upper bound

    Return:
        Index of the item if found, otherwise -1

    Examples:
    >>> binary_search([1,2,3], 0, 2, 3)
    2
    >>> binary_search([5,6,7,10], 0, 3, 45)
    -1
    >>> binary_search([], 0, 0, 2)
    -1
    """

    if (high < low) or len(arr) == 0:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid+1, high, target)
    else:
        return binary_search(arr, low, mid-1, target)

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input('Enter numbers separated by commas:\n').strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    key = int(input("Enter the value to be searched:\n").strip())

    RESULT = binary_search(collection, 0, len(collection)-1, key)

    if RESULT == -1:
        print(f"{key} not present in {collection}")
    else:
        print(f"{key} found at location {RESULT}")
