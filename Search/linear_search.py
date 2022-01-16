"""
A pure python implementation of linear search algorithm.

Time Complexity:
    - Best Case: 𝛩(1)
    - Worst Case: 𝛩(n); where n is the number of element in the array

For doctests run following command:
python -m doctest -v linear_search.py

For manual testing run:
python linear_search.py
"""

def linear_search(arr: list, target: int) -> int:
    """
    Iterative method of implementing linear search

    Params:
    arr: some mutable ordered collection with heterogeneous comparable items inside
    target: item value to search

    Return:
    Index of found item or -1 if item not found

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

    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    user_input = input("Enter numbers separated by comma:\n")
    key = int(input("Enter a single number to be searched in the list: ").strip())

    if len(user_input) == 0:
        RESULT = -1
    else:
        sequence = list(map(int, user_input.split(",")))
        RESULT = linear_search(sequence, key)
    
    if RESULT != -1:
        print(f"Item found at location {RESULT}")
    else:
        print(f"{key} was not found in the list")