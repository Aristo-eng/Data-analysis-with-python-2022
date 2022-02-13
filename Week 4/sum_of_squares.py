def sum_of_squares(lst):
    "Computes the sum of squares of elements in the list given as parameter"
    s=0
    for x in lst:
        s=s+x**2
    return s

print("The docsting is: ", sum_of_squares.__doc__)
print(sum_of_squares([-2]))
print(sum_of_squares([-2,4,5]))