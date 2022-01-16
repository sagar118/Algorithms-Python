"""
A pure python implementation of selection sort.

Time Complexity:
    - Best Case: 𝛩(n²)
    - Worst Case: 𝛩(n²)
"""

def selection_sort(arr: list) -> list:
    """
    Params:
    arr: some mutable ordered collection with heterogeneous comparable items inside
    
    Return: 
    The same arr sorted in ascending order

    Examples (non-decreasing order):
    >>> selection_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> selection_sort([]) == sorted([])
    True
    >>> selection_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> selection_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> selection_sort(collection) == sorted(collection)
    True
    """

    lenArray = len(arr)
    for index in range(lenArray - 1):
        minIndex = index
        for j in range(index+1, lenArray):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        if minIndex != index:
            arr[minIndex], arr[index] = arr[index], arr[minIndex]
    return arr

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    user_input = input("Enter the numbers separated by comma:\n").strip()

    if len(user_input) == 0:
        sorted_arr = []
    else:
        sequence = list(map(int, user_input.split(",")))
        sorted_arr = selection_sort(sequence)
    
    print(f"Sorted array: {sorted_arr}")
