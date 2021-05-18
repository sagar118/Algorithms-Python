
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        """Initialize the head of the linked list to None"""
        self.head = None

    def __iter__(self):
        """Loop through the linked list"""
        node = self.head
        while node:
            yield node.data
            node = node.next
    
    def __len__(self) -> int:
        """Length of linked list"""
        return len(tuple(iter(self)))
    
    def __repr__(self) -> str:
        """String representation of linked list"""
        return "->".join([str(item) for item in self])
    
    def __getitem__(self, index) -> Node:
        """Return value of the node based on the index"""
        if not 0 <= index < len(self):
            raise IndexError("List index out of range")
        for i, node in enumerate(self):
            if i == index:
                return node
    
    def __setitem__(self, index, data) -> None:
        """Update the value of the node based on the index"""
        if not 0 <= index < len(self):
            raise IndexError("List index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data
    
    def insert_nth(self, index: int, data) -> None:
        """Insert a new node at index n"""
        if not 0 <= index <= len(self):
            raise IndexError("List index out of range")
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node        
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
    
    def insert_head(self, data) -> None:
        """Insert node a the head i.e. at the start of the linked list"""
        self.insert_nth(0, data)
    
    def insert_tail(self, data) -> None:
        """Insert a new node at the end of the linked list"""
        self.insert_nth(len(self), data)
    
    def delete_nth(self, index: int) -> int:
        """Delete a node from the linked list at the given index"""
        if not 0 <= index <= len(self) - 1:
            raise IndexError("List index out of range")
        
        delete_node = self.head
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data
    
    def delete_head(self) -> int:
        """Delete node present at the head of the linked list"""
        return self.delete_nth(0)

    def delete_tail(self) -> int:
        """Delete node present at the tail of the linked list"""
        return self.delete_nth(len(self) - 1)

    def print_list(self) -> str:
        """Display the whole linked list"""
        print(self)
    
    def is_empty(self) -> bool:
        """Check if linked list is empty"""
        return self.head is None
    
    def reverse(self) -> str:
        """Perform the reverse operation on the linked list"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    linked_list = LinkedList()
    assert linked_list.is_empty() is True
    assert str(linked_list) == ""

    try:
        linked_list.delete_head()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        linked_list.delete_tail()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(linked_list) == i
        linked_list.insert_nth(i, i + 1)
    assert str(linked_list) == "->".join(str(i) for i in range(1, 11))

    linked_list.insert_head(0)
    linked_list.insert_tail(11)
    assert str(linked_list) == "->".join(str(i) for i in range(0, 12))

    assert linked_list.delete_head() == 0
    assert linked_list.delete_nth(9) == 10
    assert linked_list.delete_tail() == 11
    assert len(linked_list) == 9
    assert str(linked_list) == "->".join(str(i) for i in range(1, 10))

    assert all(linked_list[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        linked_list[i] = -i
    assert all(linked_list[i] == -i for i in range(0, 9)) is True

if __name__ == "__main__":
    from doctest import testmod

    testmod()

    linked_list = LinkedList()
    linked_list.insert_head(input("Inserting node at head: ").strip())
    linked_list.insert_head(input("Inserting node at head: ").strip())
    print("\nPrint list:")
    linked_list.print_list()
    linked_list.insert_tail(input("\nInserting node at tail: ").strip())
    linked_list.insert_tail(input("Inserting node at tail: ").strip())
    
    insert_index = int(input("Insert at index: ").strip())
    linked_list.insert_nth(insert_index, input(f"Inserting node at index {insert_index}: ").strip())
    
    print("\nPrint list:")
    linked_list.print_list()
    print("\nDelete head")
    linked_list.delete_head()
    print("Delete tail")
    linked_list.delete_tail()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nReverse linked list")
    linked_list.reverse()
    print("\nPrint list:")
    linked_list.print_list()
    print("\nString representation of linked list:")
    print(linked_list)
    print("\nReading/changing Node data using indexing:")
    change_index = int(input("Change node value at index: ").strip())
    print(f"Element at Position {change_index}: {linked_list[change_index]}")
    linked_list[change_index] = input("Enter New Value: ").strip()
    print("New list:")
    print(linked_list)
    print(f"length of linked_list is : {len(linked_list)}")