def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(2,7):
         l.append(i)
    return l 
print(main(2,7))