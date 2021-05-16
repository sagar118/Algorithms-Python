"""
A pure python implementation of bucket sort. Bucket sort is mainly useful when input is uniformly 
distributed over a range.
"""

def insertion_sort(arr: list) -> list:
    """
    Insertion sort used to sort values in each bucket

    Params:
        arr: A mutable collection that represent values in each bucket
    
    Returns:
        sCollection in sorted order
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def bucket_sort(arr: list) -> list:
    """
    This function implements bucket sort algorithm. To sort value in each bucket we use insertion 
    sort algorithm.

    Params:
        arr: A mutable collection which needs to be sort
    
    Returns:
        The same collection in sorted order

    Examples:
    >>> data = [-1, 2, -5, 0]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> data = [9, 8, 7, 6, -12]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> data = [.4, 1.2, .1, .2, -.9]
    >>> bucket_sort(data) == sorted(data)
    True
    >>> bucket_sort([]) == sorted([])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 50)
    >>> bucket_sort(collection) == sorted(collection)
    True
    """
    if len(arr) == 0:
        return []
    
    max_value = max(arr)
    min_value = min(arr)

    range_of_elements = max_value - min_value
    no_of_bucket = int(range_of_elements) + 1

    # Create empty buckets
    buckets = [[] for _ in range(no_of_bucket)]

    # Add the values to the correct buckets. It also handles values with integer part
    for value in arr:
        buckets[int(value - min_value) // no_of_bucket].append(value)

    # Sort each bucket using insertion sort
    for i in range(no_of_bucket):
        buckets[i] = insertion_sort(buckets[i])
    
    # Combine sorted values in each bucket to get the final sorted collection
    result = [value for bucket_no in range(no_of_bucket) for value in buckets[bucket_no]]

    return result

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [float(item.strip()) for item in user_input.split(",")]

    result = bucket_sort(collection)
    print(f"Sorted list: {result}")