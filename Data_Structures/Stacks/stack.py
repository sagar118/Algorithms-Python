"""
A stack is an abstract data type that serves as a collection of
elements with two principal operations: push() and pop(). push() adds an
element to the top of the stack, and pop() removes an element from the top
of a stack. The order in which elements come off of a stack are
Last In, First Out (LIFO).
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
"""

class StackOverflowError(BaseException):
    pass

class StackUnderflowError(BaseException):
    pass

class Stack:
    """Stack with a fixed capacity"""

    def __init__(self, limit: int = 10):
        """Initialize a empty stack"""

        self.stack = list()
        self.limit = limit
    
    def push(self, value: int) -> None:
        """Push an element at the top of the stack"""
        if self.is_full():
            raise StackOverflowError
        self.stack.append(value)
    
    def pop(self) -> int:
        """Pop an element from top of the stack"""
        if self.is_empty():
            raise StackUnderflowError
        return self.stack.pop()
    
    def peek(self)  -> int:
        """Peek at the top-most element of the stack."""
        return self.stack[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty"""
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def is_full(self) -> bool:
        """Check if stack is full"""
        if len(self.stack) >= self.limit:
            return True
        else:
            return False
      
    def display(self) -> list:
        """Display at the whole stack"""
        return self.stack
    
    def __contains__(self, item) -> bool:
        """Check if item is in stack"""
        return item in self.stack

def test_stack() -> None:
    """
    >>> test_stack()
    """
    stack = Stack()
    assert stack.is_empty() is True
    assert stack.is_full() is False

    try:
        _ = stack.pop()
        assert False # This should not happen
    except StackUnderflowError:
        assert True # This should happend
    
    for i in range(10, 20):
        stack.push(i)
    
    try:
        stack.push(20)
        assert False # This should not happen
    except StackOverflowError:
        assert True # This should happen

    assert 11 in stack
    assert 20 not in stack

    assert stack.display() == [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert stack.is_full() is True
    assert stack.pop() == 19
    assert stack.peek() == 18

if __name__ == '__main__':
    from doctest import testmod

    testmod()
