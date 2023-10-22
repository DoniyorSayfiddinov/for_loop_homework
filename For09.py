def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    l=[]
    s=price
    for i in range(10):
        if i==0:
            l.append(price)
        else :
            s+=price
            l.append(s)
    return l
print(main(2.25))
 
    
   