"""
A pure implementation of radix sort. We have used counting sort to sort from the least significant 
bit to the most significant bit. Counting sort is a stable sort algorithm i.e. the original order
of the elements is maintained.

This program doesn't take into consideration of negative numbers.
"""

def counting_sort(arr: list, place: int) -> None:
    """
    Counting sort algorithm to sort the element by each digit.
    """
    coll_len = len(arr)
    counting_arr = [0] * 10 # Create the counting array
    output_arr = [0] * coll_len # Create the output array

    # Count how many times an element at place(unit) appears in the collection
    for i in range(coll_len):
        index = arr[i] // place
        counting_arr[index % 10] += 1

    # Sum each position with it's predecessors, that gives us the number of elements less than or
    # equal to i
    for i in range(1, len(counting_arr)):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]
    
    # Place the element in the correct position in the output arr in the original order 
    # (stable sort) from end to start
    i = coll_len - 1
    while i >= 0:
        index = arr[i] // place
        output_arr[counting_arr[index % 10] - 1] = arr[i]
        counting_arr[index % 10] -= 1
        i -= 1
    
    for i in range(coll_len):
        arr[i] = output_arr[i]

def radix_sort(arr: list) -> list:
    """
    Main prodecure of radix sort.

    Examples:
    >>> radix_sort([5, 1, 4, 2, 0, 3]) == sorted([5, 1, 4, 2, 0, 3])
    True
    >>> radix_sort([]) == []
    True
    """
    if len(arr) == 0:
        return []

    max_element = max(arr)
    place = 1

    while max_element // place > 0:
        counting_sort(arr, place)
        place *= 10
    
    return arr

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    result = radix_sort(collection)
    print(f"Sorted list: {result}")
