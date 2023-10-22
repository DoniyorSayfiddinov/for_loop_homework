def main(n):
    """
    Return numbers from zero to n in a string view.
    Args:
        n: int
    Returns:
        string: return  answer
    """
    l=''
    for i in range(3):
        if i==2:
            l+=(str(int(i)))
        else :
            l+=(str(int(i)))+','
    return l
print(main(3))