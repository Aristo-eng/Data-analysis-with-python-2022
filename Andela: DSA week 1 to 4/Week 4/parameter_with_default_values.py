def length(*t, degree=2):
    """Computes the length of the vector given as parameter. By default, it computes
    the Euclidean distance (degree==2)"""
    s=0
    for x in t:
        s += abs(x)**degree
    return s**(1/degree)


print(length(-4,3))
print(length(-4,3, degree=3)) # https://www.math.usm.edu/lambers/mat169/fall09/lecture17.pdf


'''

With the default parameter this is the Euclidean distance, and if p≠2 it is called p-norm.

We saw that it was possible to use packing and unpacking of arguments with the notation, when one wants

to specify arbitrary number of positional arguments*. This is also possible for arbitrary number of named

arguments with the ** notation. We will talk about this more in the data structures section.

'''