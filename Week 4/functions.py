# A doubling function.

def double(x):
    "This function multiplies its argument by two."
    return x*2

def sum_of_squares(a, b):
    "Computes the sum of arguments squared"
    return a**2 + b**2




if __name__=='__main__':
    print(double(4), double(1.2), double("abc"))

    # print the docstring
    print("The docstring is : " , double.__doc__) # or use help(double)  help(print)
    
    print(sum_of_squares(3, 4))
