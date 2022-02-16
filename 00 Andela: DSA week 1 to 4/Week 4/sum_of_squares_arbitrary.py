
def sum_of_squares(*t):
    "Computes the sum of squares of arbitrary number of arguments"
    s = 0
    for x in t:
        s += x**2
    return s 

print(sum_of_squares.__doc__)
print(sum_of_squares(-2))
print(sum_of_squares(-2,4,5))


'''
The strange looking argument notation (the star) is called argument packing.
It packs all the given positional arguments into a tuple t.
We will encounter tuples again later, but it suffices now to say that tuples are immutable lists. 
With the for loop we can iterate through all the elements in the tuple.


'''