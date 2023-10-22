def main(A,B):
    """
    Return the sum of all integers from A to B.
    Args:
        A: int
        B: int
    Returns:
        int: return  answer
    """
    l=0
    for i in range(A,B,):
        l+=i
    return l
print(main(3,6))