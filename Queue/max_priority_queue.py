"""
A pure implementation of priority queue using heap data structure. A priority queue is a data 
structure for maintaining a set S of elements, each with an associated value called a key. Here the 
priority queue is build using the max heap property. A max-priority queue supports the following 
operations:

1. Insert(S, x): inserts the element x into the set S, which is equivalent to the opeation S = S U {x}
2. Maximum(S): returns the element of S with the largest key
3. Extract-Max(S): removes and returns the element of S with the largest key
4. Increase-Key(S, x, k): increases the value of element x's key to the new value k, which is assumed
to be at least as large as x's current key value

Alternatively, a min-priority queue supports the oprations Insert, Minimum, Extract-Min, and 
Decrease-Key.
"""

def heap_maximum(arr: list) -> int:
    """
    Retuns the maximum value in the heap in case of max-heap i.e. at the root of the heap.

    Params:
        arr: A mutable collection
    
    Returns:
        Root value of the heap i.e. the maximum element in case of max-heap
    """
    return arr[0]

def max_heapify(arr: list, index: int, heap_size: int) -> list:
    """
    This function is responsible maintain the max heap sort property.

    Params:
        arr: A mutable collection
        index: Index of the node where we want to check wheather the max heap property is
        maintained or not.
        heap_size: Size of the heap
    
    Returns:
        The same mutable collection that follows the max heap property
    """
    left = index * 2 + 1
    right = index * 2 + 2
    largest = index

    if left <= heap_size and arr[left] > arr[index]:
        largest = left
    
    if right <= heap_size and arr[right] > arr[largest]:
        largest = right
    
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        max_heapify(arr, largest, heap_size)
    return arr

def heap_extract_max(arr: list, heap_size: int) -> int and list:
    """
    Extracts and removes the maximum value from the heap i.e. the root value. After removing the 
    maximum value the max_heapify function is called to maintain the max heap property.

    Params:
        arr: A mutable collection
        heap_size: Size of the heap
    
    Returns:
        maximum: Maximum value on the heap i.e. the root value
        arr: The same mutable collection after the maximum value is removed and the max heap 
        property is maintained.
    """
    if heap_size < 1:
        print("Heap underflow")
    
    maximum = arr[0]
    arr[0] = arr[heap_size]
    arr.pop(-1)
    heap_size -= 1
    arr = max_heapify(arr, 0, heap_size)
    print(arr)
    return maximum, arr

def find_parent_index(index: int) -> int:
    """
    Finds the parent index of any given node.
    
    Params:
        index: Index of the node of which parent index needs to be found

    Returns:
        parent_index: Parent index of the node
    """
    if index % 2 == 0:
        parent_index = index//2 - 1
    else:
        parent_index = index//2
    return parent_index

def heap_increase_key(arr: list, index: int, key: int) -> list:
    """
    Increases the value of the node based on the index with the given key value. The key value 
    should be more than the current node value otherwise an error is thrown.

    Params:
        arr: A mutable collection
        index: Index of the node whose value needs to be increased
        key: New value of the node

    Returns:
        arr: The same mutable collection with the new value at the node based on index.
    """
    if key < arr[index]:
        print("New key is smaller than currect key")
    
    arr[index] = key
    parent_index = find_parent_index(index)

    while index >= 0 and parent_index >= 0 and arr[parent_index] < arr[index]:
        arr[index], arr[parent_index] = arr[parent_index], arr[index]
        index = parent_index
        parent_index = find_parent_index(index)
    return arr

def max_heap_insert(arr: list, key: int, heap_size: int) -> list:
    """
    Inserts a new value to the heap. After the value is added heap_increase_key is called to 
    maintain the max heap property.

    Params:
        arr: A mutable collection
        key: Value of the new node
        heap_size = Size of the heap
    
    Returns:
        arr: The same mutable collection with the new value added and the heap maintains the max 
        heap property.
    """
    heap_size += 1
    arr.append(float('-inf'))
    heap_increase_key(arr, heap_size, key)
    return arr

def options(option: int, arr: list) -> int or list:
    """
    Function which is a switch case, handles which function needs to be called based on the user 
    input.

    Params:
        option: User input which maps to the switch case below
        arr: A mutable collection

    Returns:
        Calls the appropriate function based on the user input and returns the value based on 
        each function call.  
    """
    heap_size = len(arr) - 1

    if option == 2:
        index = int(input("Enter a value of index of which value needs to be increased: ").strip())
        key = int(input("Enter a value to increase the node value with: ").strip())
    elif option == 3:
        key = int(input("Enter the value of the new node: ").strip())

    switcher = {
        0: lambda: heap_maximum(arr),
        1: lambda: heap_extract_max(arr, heap_size),
        2: lambda: heap_increase_key(arr, index, key),
        3: lambda: max_heap_insert(arr, key, heap_size)
    }
    func = switcher.get(option, lambda: "Invalid option")
    return func()

if __name__ == '__main__':

    user_input = input("Enter numbers separated by commas:\n").strip()
    collection = [int(item.strip()) for item in user_input.split(",")]
    
    user_option = int(input("Select any one option from below:\n0. Maximum Lookup\n1. Extract Maximum\n\
2. Increase value of node\n3. Insert new node\n4. Exit\nEnter your option: "))

    heap_size = len(collection) - 1
    for index in range(len(collection)//2-1, -1, -1):
        max_heapify(collection, index, heap_size)
    
    while user_option >= 0 and user_option < 4:
        if user_option == 1:
            maximum, collection = options(user_option, collection)
            print(maximum)
        else:
            print(options(user_option, collection))

        print(f'Values in Heap: {collection}\n')
        
        user_option = int(input("Select any one option from below:\n0. Maximum Lookup\n1. Extract \
Maximum\n2. Increase value of node\n3. Insert new node\n4. Exit\nEnter your option: "))
