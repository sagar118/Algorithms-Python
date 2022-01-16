"""
Consider the problem of adding two n-bit binary integers, stored in two n-element arrays A and B. The sum of the two integers should be stored in binary form in an (n+1) element array C.
"""

def cal_sum(A: list, B: list) -> list:
    """
    Params:
    A: some mutable ordered collection with only 1's and 0's inside
    B: some mutable ordered collection with only 1's and 0's inside

    Result:
    Addition of two n-bit binary integer

    Examples:
    >>> cal_sum([1, 0, 1], [1, 1, 1])
    [1, 1, 0, 0]
    """
    carry = 0
    output = list()
    for index in range(len(A)-1, -1, -1):
        output.insert(0, (A[index] + B[index] + carry) % 2)
        if  A[index] + B[index] + carry >= 2:
            carry = 1
        else:
            carry = 0
    
    if carry == 1:
        output.insert(0, 1)
    return output

if __name__ == "__main__":
    from doctest import testmod

    testmod()
    
    arr1 = list(map(int, input("Enter the first n-element binary integer separated by commas:\n").split(",")))
    arr2 = list(map(int, input("Enter the second n-element binary integer separated by commas:\n").split(",")))

    result = cal_sum(arr1, arr2)
    print(f"Summation of {arr1} and {arr2} is {result}")