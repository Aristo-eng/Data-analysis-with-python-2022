
def sum_of_squares(*t):
    "Computes the sum of squares of arbitrary number of arguments"
    s = 0
    for x in t:
        s += x**2
    return s 

print(sum_of_squares.__doc__)
print(sum_of_squares(-2))
print(sum_of_squares(-2,4,5))
