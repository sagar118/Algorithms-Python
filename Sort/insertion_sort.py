"""
A pure python implementation of insertion sort algorithm.

It is an efficient algorithm for sorting a small number of elements. The algorithm sorts the input number in place.

For non-increasing order:
Change the sign from > to < in line 31 for the condition arr[index] > value. Also, comment line 41.

Time Complexity:
    - Best Case: 𝛩(n)
    - Worst Case: 𝛩(n²)

For doctests run following command:
python -m doctest -v insertion_sort.py

For manual testing run:
python insertion_sort.py
"""

def insertion_sort(arr: list) -> list:
    """
    Params:
    arr: some mutable ordered collection with heterogeneous comparable items inside
    
    Return: 
    The same arr sorted in ascending order

    Examples (non-decreasing order):
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

    for index, value in enumerate(arr[1:]):
        while (index >= 0) and (arr[index] > value):
            arr[index+1] = arr[index]
            index -= 1
        arr[index+1] = value
    return arr

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    user_input = list(map(int, input("Enter the numbers separated by comma:\n").split(",")))
    sorted_arr = insertion_sort(user_input)
    print(f"Sorted arr: {sorted_arr}")