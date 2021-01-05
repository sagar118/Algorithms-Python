"""
A pure Python implementation of the insertion sort algorithm

For doctests run following command:
python -m doctest -v insertion_sort.py

For manual testing run:
python insertion_sort.py
"""

def insertion_sort(arr: list) -> list:
    """
    :param arr: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same arr ordered by ascending

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([]) == sorted([])
    True
    >>> insertion_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> insertion_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    """

    for index, item in enumerate(arr[1:]):
        while (index >= 0) and (arr[index] > item):
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = item
    return arr

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = list(map(int, input('Enter numbers seperated by commas:\n').split(",")))
    sorted_arr = insertion_sort(user_input)
    print(f"Sorted array: {sorted_arr}")
