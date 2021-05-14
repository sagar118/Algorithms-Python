"""
A pure python implementation of heap sort algorithm. Here, we have sorted the input using the 
max heap property.
"""

def max_heapify(arr: list, index: int, heap_size: int) -> None:
    """
    This function is responsible maintain the max heap sort property.

    Params:
        arr: A mutable collection
        index: Index of the node where we want to check wheather the max heap property is
        maintained or not.
        heap_size: Size of the heap
    """
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left <= heap_size and arr[left] > arr[index]:
        largest = left
    
    if right <= heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        max_heapify(arr, largest, heap_size)

def build_max_heap(arr: list) -> None:
    """
    This function is responsible to build the max heap from an unsorted array
    
    Params:
        arr: A mutable collection where values are unsorted
    """
    heap_size = len(arr) - 1
    for index in range(len(arr)//2-1, -1, -1):
        max_heapify(arr, index, heap_size)

def heap_sort(arr: list) -> list:
    """
    This function is responsible to sort the input using the heap sort technique. Heap sort is a 
    technique that sorts the input in place.

    Params:
        arr: A mutable collection
    
    Returns:
        The same collection sorted in ascending order.
    
    Examples:
    >>> heap_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> heap_sort([])
    []
    >>> heap_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    heap_size = len(arr) - 1
    build_max_heap(arr)
    for index in range(len(arr)-1, 0, -1):
        arr[index], arr[0] = arr[0], arr[index]
        heap_size -= 1
        max_heapify(arr, 0, heap_size)
    return arr

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]

    result = heap_sort(collection)
    print(f"Sorted list: {result}")