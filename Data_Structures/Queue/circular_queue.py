"""
Cicular Queue is a linear data structure in which operations are performed based on FIFO (First In 
First Out) principle.
"""

class QueueOverflowError(BaseException):
    """Queue is full"""
    def __init__(self):
        self.message = "Queue is Full!!"
    
    def __str__(self):
        return self.message

class QueueUnderflowError(BaseException):
    """Queue is empty"""
    def __init__(self):
        self.message = "Queue is Empty!!"
    
    def __str__(self):
        return self.message

class CircularQueue:
    """Cicular queue with a fixed capacity"""

    def __init__(self, limit: int = 10):
        """Initialize the queue with None"""
        
        self.limit = limit
        self.queue = [None] * self.limit
        self.front = self.rear = -1
    
    def enqueue(self, value: int) -> None:
        """
        Add value into the queue at the rear position.

        Params:
            value: Value to be inserted in the queue
        """  
        if ((self.rear + 1) % self.limit) == self.front:
            raise QueueOverflowError
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.limit 
            self.queue[self.rear] = value
    
    def dequeue(self) -> int:
        """
        Removes the value present at the front position

        Returns:
            The value removed at the front position
        """
        if (self.front == -1):
            raise QueueUnderflowError
        elif self.front == self.rear:
            value = self.queue[self.front]
            self.front = self.rear = -1
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.limit
        return value
    
    def peek(self):
        if self.front != -1:
            return self.queue[self.front]
        else:
            print('Queue is empty')

    def display(self) -> None:
        """Prints the values in the cicular queue"""

        if self.front == -1:
            print('Queue is empty')
        elif self.rear >= self.front:
            for index in range(self.front, self.rear + 1):
                print(self.queue[index], end=" ")
            print()
        else:
            for index in range(self.front, self.limit):
                print(self.queue[index], end=" ")
            for index in range(self.rear + 1):
                print(self.queue[index], end=" ")
            print()                 

def test_cqueue():
    """
    >>> test_cqueue()
    """
    queue = CircularQueue(10)

    try:
        _ = queue.dequeue()
        assert False
    except QueueUnderflowError:
        assert True

    for item in range(10):
        queue.enqueue(item)
    
    assert queue.peek() == 0
    try:
        _ = queue.enqueue(10)
        assert False
    except QueueOverflowError:
        assert True

    assert queue.dequeue() == 0

if __name__ == '__main__':
    from doctest import testmod

    testmod()

    queue = CircularQueue(5)
    queue.enqueue(14)
    queue.enqueue(22)
    queue.enqueue(13)
    queue.enqueue(-6)
    queue.display()
    print ("Deleted value = ", queue.dequeue())
    print ("Deleted value = ", queue.dequeue())
    queue.display()
    queue.enqueue(9)
    queue.enqueue(20)
    queue.enqueue(5)
    queue.display()