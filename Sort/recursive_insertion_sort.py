"""
A pure python implementation of recursion sort
"""

def recursive_insertion_sort(arr: list, num: int) -> list:
    """
    Params:
        arr: A mutable collection
        num: Number of elements in arr

    Returns:
        The same collection in sorted order

    Examples:
    >>> recursive_insertion_sort([0, 5, 3, 2, 2], 5)
    [0, 2, 2, 3, 5]
    >>> recursive_insertion_sort([], 0) == sorted([])
    True
    >>> recursive_insertion_sort([-2, -5, -45], 3) == sorted([-2, -5, -45])
    True
    >>> recursive_insertion_sort(['d', 'a', 'b', 'e', 'c'], 5) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> recursive_insertion_sort(collection, 100) == sorted(collection)
    True
    """

    # Single element is already in sorted order
    if num == 1:
        return None
    elif num < 1:
        return []

    # Call the function recursively to sort first n-1 elements
    recursive_insertion_sort(arr, num-1)

    last_val = arr[num-1]
    pos = num-2

    while (pos >= 0) and (arr[pos] > last_val):
        arr[pos+1] = arr[pos]
        pos -= 1
    arr[pos+1] = last_val

    return arr

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = list(map(int, input('Enter numbers seperated by commas:\n').split(",")))
    sorted_arr = recursive_insertion_sort(user_input, len(user_input))
    print(f"Sorted array: {sorted_arr}")
