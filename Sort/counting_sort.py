"""
A pure python implementation of counting sort. Here we have tweaked the sorting algorithm to handle
negative numbers as well.

Counting sort is not a comparision based sorting algorithms. It's time complexity is O(n+k). It is 
often used as a subroutine to another algorithm like radix sort.
"""
def counting_sort(arr: list) -> list:
    """
    Main function of counting sort algorithm.

    Params:
        arr: A mutable collection that needs to be sorted
    
    Returns:
        The same collection in sorted order
    
    Examples:
    >>> counting_sort([5, 1, 4, 2, 0, 3])
    [0, 1, 2, 3, 4, 5]
    >>> counting_sort([])
    []
    >>> counting_sort([-22, 0, -2, 1])
    [-22, -2, 0, 1]
    """
    if arr == []:
        return []

    coll_len = len(arr)
    max_element = max(arr)
    min_element = min(arr)
    range_of_elements = max_element - min_element + 1

    # Create the counting array
    counting_arr = [0] * range_of_elements

    # Create the output array
    output_arr = [0]  * coll_len

    # Count how many times an element appears in the collection
    for number in arr:
        counting_arr[number - min_element] += 1
    
    # Sum each position with it's predecessors, that gives us the number of elements less than or
    # equal to i
    for i in range(1, range_of_elements):
        counting_arr[i] = counting_arr[i] + counting_arr[i-1]
    
    # Place the element in the correct position in the output arr in the original order 
    # (stable sort) from end to start
    for i in range(coll_len-1, -1, -1):
        output_arr[counting_arr[arr[i] - min_element] - 1] = arr[i]
        counting_arr[arr[i] - min_element] -= 1

    return output_arr

def counting_sort_string(string: str) -> str:
    """
    Handle string values

    Examples:
    >>> counting_sort_string("acedbf")
    'abcdef'
    """
    return "".join([chr(i) for i in counting_sort([ord(c) for c in string])])

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    result = counting_sort(collection)
    print(f"Sorted list: {result}")